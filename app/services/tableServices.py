import pandas as pd
from app.database import engine
from app.database import SessionLocal
from app.database.workers import WorkerPosition, Worker
from app.database.operations import Operation


def fetchDataFromDb(tableName):
    """ Fetches data from PostgreSQL table """
    with engine.connect() as conn:
        df = pd.read_sql(f'SELECT * FROM "{tableName}";', conn)
    return df


def fetchDataFromDbWithRelations(tableName):
    """ Fetches data from PostgreSQL table with related data """
    if tableName == 'workers':
        session = SessionLocal()
        try:
            column = "Група"
            df = fetchDataFromDb(tableName)
            for index, item in enumerate(df[column]):
                # print(f"index: {index}, item: {item}")
                if not pd.isna(item):
                    workerGroup = session.query(Worker).filter(Worker.Група == item).first()
                    df.at[index, column] = workerGroup.cehove.Група
            session.close()
            return df
        except Exception as e:
            print(f"Error fetching data from database: {e}")
            return fetchDataFromDb(tableName)
        finally:
            session.close()

    elif tableName == 'operations':
        session = SessionLocal()
        try:
            result = session.query(Operation).all()
            data = []
            for item in result:
                data.append({
                    'ОперацияNo': item.ОперацияNo,
                    'Операция': item.Операция,
                    'ОперацияТип': item.operationTypes[0].OperName if item.operationTypes else '',
                })
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            print(f"Error fetching data from database: {e}")
        finally:
            session.close()

    elif tableName == 'workerPositions':
        session = SessionLocal()
        try:
            result = session.query(WorkerPosition).all()

            data = []
            for item in result:
                data.append({
                    'ДлъжностКод': item.ДлъжностКод,
                    'Длъжност': item.Длъжност,
                    'Коефициент': item.Коефициент,
                    'ВидОперация': item.operationType.OperName if item.operationType else ''
                })
            df = pd.DataFrame(data)
            session.close()
            return df
        except Exception as e:
            print(f"Error fetching data from database: {e}")
            return fetchDataFromDb(tableName)
        finally:
            session.close()
    else:
        return fetchDataFromDb(tableName)
