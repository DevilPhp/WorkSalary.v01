from datetime import datetime

import pyodbc
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text, Column, MetaData, Table, String, DateTime, Integer, Double, Boolean, \
    BINARY, ForeignKey
from config import DATABASE_URL
from app.database import SessionLocal
from app.database.workers import OperationType, PaymentType, Cehove
from app.database.operations import modelOperationsType
from app.database.models import ProductionModel

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
    # for table in cursor.fetchall()
    if table_name == "cehove":
        df = pd.read_sql(f"SELECT * FROM {table_name} ORDER BY {'Група'}", conn)
    elif table_name == "Модел и оперции":
        df = pd.read_sql(f'''SELECT * FROM "{table_name}"''', conn)
        df = df[df['Операция'].notna() & (df['Операция'] != '') & (df['LastModified'] >= '2024-10-01 00:00:00')]
        # & (df['LastModified'] <= '2025-01-01 00:00:00')
    else:
        df = pd.read_sql(f'''SELECT * FROM "{table_name}"''', conn)

    # Query to get table structure
    # df = pd.read_sql(f"SELECT * FROM {table_name} ORDER BY {'Група'}", conn)
    cursor.execute(f'''SELECT * FROM "{table_name}" WHERE 1=0''')  # Fetch only metadata
    # print(df)
    # return
    # columns = [(column[0], map_data_type(column[1])) for column in cursor.description]
    conn.close()
    # print(df['LastModified'])
    # print(len(df))
    return df


def insert_data_to_postgres_with_fkey(table_name, df):
    # df = df.drop(columns=['TRid'], inplace=True)
    """ Inserts data into a PostgreSQL table """
    session = SessionLocal()
    # print(df)
    try:
        for col, row in df.iterrows():
            # print(row)
            operType = session.query(OperationType).get(row['OpTypeId'])
            # newOperation = modelOperationsType(
            #     ModelOpID=row,
            # )

            # return
    except Exception as e:
        print(f"Error occurred: {e}")
        return
    finally:
        session.close()
    # engine = create_engine(DATABASE_URL)
    # with engine.connect() as conn:
    #     # result = conn.execute(text("SELECT COUNT(*) FROM operationTypes WHERE OperTypeID = 0"))
    #     # if result.scalar() == 0:
    #     #     conn.execute(text("INSERT INTO operationTypes (OperTypeID, OperName) VALUES (0, '')"))
    #     #     conn.commit()
    #     df.to_sql(table_name, conn, if_exists="append", index=False)
    #     print(f"✅ {len(df)} records inserted into '{table_name}' successfully!")


def checkForColumns(table_name, df):
    if table_name == 'clients':
        culumns = ["КодСчетоводство", "СчетПоръчка"]
        df.drop(columns=culumns, inplace=True)

    elif table_name == 'vidOblekla':
        df.drop(columns=['WearTyp'], inplace=True)

    elif table_name == 'operations':
        df.drop(columns=['ТипОперация'], inplace=True)

    elif table_name == 'modelOperationsTypes':
        df.drop(columns=['TRid'], inplace=True)

    elif table_name == 'machines':
        columns = {
            "MashineTyp": "MachineType",
            "MachFine": "MachineFine",
            "MachSys": "MachineSystem",
        }
        df.rename(columns=columns, inplace=True)

    elif table_name == 'productionModels':
        df.drop(columns=['ОблеклоВид', 'ЦелГрупа', 'ЗаповедNo', 'ЗаповедДата', 'Picture', 'ModelNoPlanSys',
                         'СтаусВръзка'], inplace=True)
        columns = {
            'MashTyp': 'MachineId',
            'WearTyp': 'WearType',
            'YarnTyp': 'YarnType',
            'DateInpMod': 'DateCreated',
            'ModifiedBy': 'UserCreated'
        }
        df.rename(columns=columns, inplace=True)
        for index, row in enumerate(df['UserCreated']):
            if row is None:
                df.at[index, 'UserCreated'] = 'admin'
        for index, row in enumerate(df['MachineId']):
            if row == 0:
                df.at[index, 'MachineId'] = None
        for index, row in enumerate(df['Actual']):
            if row == 'y':
                df.at[index, 'Actual'] = True
            else:
                df.at[index, 'Actual'] = False

    elif table_name == 'productionModelOperations':
        # session = SessionLocal()
        df.drop(columns=['ОперацияID'], inplace=True)
        columns = {
            'ВремеЗаОп-я': 'TimeForOper',
            'LastModified': 'LastUpdated',
            'ModifiedBy': 'UpdatedBy'
        }
        df.rename(columns=columns, inplace=True)
        models = getProductionModels()
        count = 0
        zeroCount = 0
        orderIdRows = []
        for index, row in df.iterrows():
            if row['ПоръчкаNo'] in models.keys():
                # df['orderId'] = models[row['ПоръчкаNo']]
                orderIdRows.append(models[row['ПоръчкаNo']])
                # print(df.at[index, 'ПоръчкаNo'])
                # print(f"Found model with ID: {models[row]}")
                count += 1
            else:
                orderIdRows.append(None)
                zeroCount += 1
        df['OrderId'] = orderIdRows

        # print(df['orderId'])
        print(f"Found {count} models")
        print(f"Found {zeroCount} models without orderId")

    elif table_name == 'paymentPerMinutes':
        df.drop(columns=['MinuteRabID'], inplace=True)
        euroRate = 1.95584
        paymentInEuro = []
        levToEuro = []
        columns = {
            'MinuteRabVal': 'PaymentValue',
            'DateValid': 'DateActive',
            'Коментар': 'Comment',
            'LastModified': 'LastUpdated',
            'ModifiedBy': 'UpdatedBy'
        }
        df.rename(columns=columns, inplace=True)
        for index, row in enumerate(df['PaymentValue']):
            df.at[index, 'PaymentValue'] = round(row, 4)
            paymentInEuro.append(round(row / euroRate, 4))
            levToEuro.append(euroRate)
        df['PaymentInEuro'] = paymentInEuro
        df['LevToEuro'] = levToEuro

    return df

def getProductionModels():
    dictModels = {}
    session = SessionLocal()
    models = session.query(ProductionModel).all()
    for model in models:
        dictModels[model.ПоръчкаNo] = model.id
    session.close()
    return dictModels



def insert_data_to_postgres(table_name, df):

    checkForColumns(table_name, df)
    # for index, row in df.iterrows():
    #     if row['orderId'] == 0 or row['orderId'] is None:
    #         print(row['orderId'])
    # return
    # return
    # print(df.columns)
    # return

    # columnsNames = {
    #     "Група": "group",
    #     "ГрупаName": "groupName",
    #     "Вид": "type",
    #     "SupervisorNo": "supervisorNo"
    # }
    # df = df.rename(columns=columnsNames)
    # df = df[list(columnsNames.values())]

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


def insertZeroOperationType():
    # engine = create_engine(DATABASE_URL)
    session = SessionLocal()
    try:
        zeroOperType = OperationType(OperTypeID=0, OperName="")
        session.add(zeroOperType)
        session.commit()
        print("Zero OperationType inserted successfully!")
    except Exception as e:
        print(f"Error inserting Zero OperationType: {str(e)}")
        session.rollback()
    finally:
        session.close()

def renameColumnsAndReplaceData(df):
    # Rename columns as required
    columnsNames = {
        "гр/с": "гр_с",
        "Трудов стаж-Години": "ТрудовСтажГодини",
        "Трудов стаж-Месеци": "ТрудовСтажМесеци",
        "Трудов стаж-Дни": "ТрудовСтажДни",
    }
    # print(df.dtypes)
    # return
    for column in df.columns:
        if column in columnsNames:
            df.rename(columns={column: columnsNames[column]}, inplace=True)
        if column == "Група":
            session = SessionLocal()
            try:
                # cehove = session.query(Cehove).order_by(Cehove.id.asc()).all()
                # for ceh in cehove:
                #     if ceh.ГрупаName in df[column]:
                #         print(f"Updating Cehove with id {ceh.id} and name {ceh.ГрупаName}")
                for index, row in enumerate(df[column]):
                    # print(cehove[index].ГрупаName)
                    # print(row)
                    if row:
                        ceh = session.query(Cehove).filter(Cehove.Група == row).first()
                        df.at[index, "Група"] = ceh.id
                    else:
                        df.at[index, "Група"] = None
                    # df.at[index, "Група"] = cehove[index].Група
                # print(df[column])
            # print(Cehove.ГрупаName)
                # df.at[index, "Група"] = Cehove[row]
                session.close()
            except Exception as e:
                print(f"Error inserting or updating Cehove data: {str(e)}")
                session.rollback()
                session.close()

        elif column == "СистемаЗаплащане":
            for index, row in enumerate(df[column]):
                if pd.isna(row):
                    df.at[index, column] = 0

    return df


def extract_and_transform_data():
    # ####Fetch data from Access table and add in to db####
    # dataCehove = fetch_access_data("cehove")
    # insert_data_to_postgres("cehove", dataCehove)
    # dataOperationTypes = fetch_access_data("operationTypes")
    # insertZeroOperationType()
    # insert_data_to_postgres("operationTypes", dataOperationTypes)
    # dataWorkersType = fetch_access_data("Длъжности")
    # insert_data_to_postgres("workerPositions", dataWorkersType)
    # dataWorkers = fetch_access_data("Персонал")
    # dataWorkers = renameColumnsAndReplaceData(dataWorkers)
    # insert_data_to_postgres("workers", dataWorkers)
    # dataClients = fetch_access_data("Клиенти")
    # insert_data_to_postgres("clients", dataClients)
    # dataOblekla = fetch_access_data("Oblekla")
    # insert_data_to_postgres("vidOblekla", dataOblekla)
    # dataYarns = fetch_access_data("Прежда")
    # insert_data_to_postgres("yarns", dataYarns)
    # dataOperations = fetch_access_data("Операции")
    # insert_data_to_postgres("operations", dataOperations)
    # dataOperType = fetch_access_data("OperTypeOfModelOper")
    # insert_data_to_postgres("modelOperationsTypes", dataOperType)
    # dataMachines = fetch_access_data("Machines")
    # insert_data_to_postgres("machines", dataMachines)
    # dataModels = fetch_access_data("Models")
    # insert_data_to_postgres("productionModels", dataModels)
    # dataModelsForOperations = fetch_access_data('Модел и оперции')
    # insert_data_to_postgres("productionModelOperations", dataModelsForOperations)  # Specify Date for shorter time
    # paymentsData = fetch_access_data("MinutaStafka")
    # insert_data_to_postgres("paymentPerMinutes", paymentsData)


    # print(data)
    # insert_data_to_postgres_with_fkey("modelOperationsTypes", data)
    # insert_data_to_postgres("operations", dataOperations)

    #####

    # Clean and transform data as needed (e.g., handling missing values, data type conversion)
    # foreign_keys = {"ВидОперация": "workerPositions.ВидОперация"}
    # Insert transformed data into PostgreSQL table
    # create_postgres_table("cehove", access_columns)
    # print(data[1])
    # insert_data_to_postgres("workerPositions", dataWorkers)
    pass



if __name__ == "__main__":
    extract_and_transform_data()
