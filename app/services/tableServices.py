import pandas as pd
from app.database import engine
def fetch_data_from_db(table_name):
    """ Fetches data from PostgreSQL table """
    with engine.connect() as conn:
        df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
    return df
