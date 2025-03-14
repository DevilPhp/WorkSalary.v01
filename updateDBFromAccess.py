import pyodbc
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

ACCESS_DB_PATH = r"E:\fedbase\ts4rep_new.accdb"
POSTGRESQL_URL = "postgresql://knitex:eb564ff0@localhost:5400/knitex"

accessConn = pyodbc.connect(
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={ACCESS_DB_PATH};"
)

accessCursor = accessConn.cursor()

pgEngine = create_engine(POSTGRESQL_URL)
pgConn = pgEngine.connect()

def getUserTables(cursor):
    return [table.table_name for table in cursor.tables(tableType='TABLE')]


tables = getUserTables(accessCursor)

# accessCursor.execute("SELECT Name FROM MSysObjects WHERE Type=1 AND Flags=0")
# tables = [row[0] for row in accessCursor.fetchall()]

# ---- FUNCTION: CONVERT ACCESS TO POSTGRESQL TYPES ----
def map_data_type(accessType):
    typeMapping = {
        "TEXT": "TEXT",
        "MEMO": "TEXT",
        "BYTE": "SMALLINT",
        "INTEGER": "INTEGER",
        "LONG": "BIGINT",
        "CURRENCY": "MONEY",
        "SINGLE": "REAL",
        "DOUBLE": "DOUBLE PRECISION",
        "DATETIME": "TIMESTAMP",
        "YESNO": "BOOLEAN",
        "OLEOBJECT": "BYTEA",
        "GUID": "UUID",
    }
    return typeMapping.get(accessType.upper(), "TEXT")  # Default to TEXT

for table in tables:
    print(f"Migrating table: {table}")

    # Get column details
    accessCursor.execute(f"SELECT * FROM {table}")
    columns = [column[0] for column in accessCursor.description]
    columnTypes = [map_data_type(str(column[1])) for column in accessCursor.description]

    # Create table in PostgreSQL
    columnsWithTypes = ", ".join(f'"{col}" {ctype}' for col, ctype in zip(columns, columnTypes))
    createTableQuery = f'CREATE TABLE IF NOT EXISTS "{table}" ({columnsWithTypes});'

    try:
        with pgEngine.connect() as connection:
            connection.execute(createTableQuery)
        print(f"Created table {table} in PostgreSQL.")
    except Exception as e:
        print(f"Error creating table {table}: {e}")

    # Fetch data from Access
    accessCursor.execute(f"SELECT * FROM {table}")
    rows = [list(row) for row in accessCursor.fetchall()]  # Convert tuples to lists
    df = pd.DataFrame(rows, columns=columns) if rows else pd.DataFrame(columns=columns)

    if rows:
        df = pd.DataFrame(rows, columns=columns)
    else:
        df = pd.DataFrame(columns=columns)

    # Insert data into PostgreSQL
    try:
        df.to_sql(table, pgEngine, if_exists="replace", index=False)
        print(f"Inserted {len(df)} rows into {table}.")
    except Exception as e:
        print(f"Error inserting data into {table}: {e}")

# ---- CLOSE CONNECTIONS ----
accessConn.close()
pgConn.close()

print("Migration completed successfully!")

