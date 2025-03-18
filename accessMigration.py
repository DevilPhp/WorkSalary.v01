from datetime import datetime

import pyodbc
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text, Column, MetaData, Table, String, DateTime, Integer, Double, Boolean, \
    BINARY, ForeignKey
from config import DATABASE_URL

ACCESS_DB_PATH = r"E:\fedbase\ts4rep_new.accdb"

# Create connection string (for Access 2016 or later, use "Microsoft.ACE.OLEDB.12.0")
conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    f"DBQ={ACCESS_DB_PATH};"
)

tables = []


def fetch_access_data(table_name):
    """ Fetch data from an MS Access table """
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Query to get table structure
    df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
    cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")  # Fetch only metadata
    columns = [(column[0], map_data_type(column[1])) for column in cursor.description]
    conn.close()
    return columns, df


def insert_data_to_postgres(table_name, df):
    # columnsNames = {
    #     "Група": "group",
    #     "ГрупаName": "groupName",
    #     "Вид": "type",
    #     "SupervisorNo": "supervisorNo"
    # }
    # df = df.rename(columns=columnsNames)
    # df = df[list(columnsNames.values())]
    if 'ВидОперация' in df.columns:
        df['ВидОперация'] = pd.to_numeric(df['ВидОперация'], errors='coerce').fillna(0).astype(int)
        print(df['ВидОперация'])

    """ Inserts data into a PostgreSQL table """
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"✅ {len(df)} records inserted into '{table_name}' successfully!")


def map_data_type(accessType):
    typeMapping = {
        str: String,
        int: Integer,
        float: Double,
        bool: Boolean,
        bytes: BINARY,
        datetime: DateTime,  # Convert datetime to ISO format
        type(None): String
    }
    return typeMapping.get(accessType, String)


def create_postgres_table(table_name, columns, foreign_keys=None):
    """ Generates a CREATE TABLE statement for PostgreSQL """
    # column_definitions = []

    # for col_name, access_type in columns:
    #     # print(access_type)
    #     postgres_type = map_data_type(access_type)
    #     print(postgres_type)
    #     column_definitions.append(f'"{col_name}" {postgres_type}')  # Handle spaces in column names
    #
    # create_table_sql = text(f'CREATE TABLE IF NOT EXISTS "{table_name}" ({", ".join(column_definitions)});')

    # Connect to PostgreSQL and execute the statement
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    column_objects = [
        Column(col_name, col_type,
               ForeignKey(foreign_keys[col_name]) if foreign_keys and col_name in foreign_keys else None)
        for col_name, col_type in columns
    ]

    table = Table(table_name, metadata, *column_objects)
    tables.append(table)
    with engine.connect() as conn:
        metadata.create_all(engine, tables=tables) # Create table if it doesn't exist already'
        print(f"Table '{table_name}' created successfully!")


def extract_and_transform_data():
    # Fetch data from Access table
    data = fetch_access_data("Длъжности")
    access_columns = data[0]

    # Clean and transform data as needed (e.g., handling missing values, data type conversion)
    foreign_keys = {"ВидОперация": "workerPositions.ВидОперация"}
    # Insert transformed data into PostgreSQL table
    # create_postgres_table("cehove", access_columns)
    # print(data[1])
    insert_data_to_postgres("workerPositions", data[1])



if __name__ == "__main__":
    extract_and_transform_data()
