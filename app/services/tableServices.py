import pandas as pd
from app.database import engine
from sqlalchemy.orm import joinedload
from app.database import SessionLocal
from app.database.workers import WorkerPosition, OperationType, Worker
from app.database.operations import Operation, modelOperationsType


def fetchDataFromDb(tableName):
    """ Fetches data from PostgreSQL table """
    with engine.connect() as conn:
        df = pd.read_sql(f'SELECT * FROM "{tableName}";', conn)
    return df


def fetchDataFromDbWithRelations(tableName, relationships=None):
    """ Fetches data from PostgreSQL table with related data """
    # try:
    #     df = pd.read_sql(f'SELECT w.*, op.* FROM "{tableName}" w LEFT JOIN "operationTypes" op'
    #                      f' ON w.id = op."OperTypeID";', session.bind)
    #     if relationships:
    #         for relationship in relationships:
    #             df = df.merge(getattr(session.class_, relationship[0]).join(getattr(session.class_, relationship[1])),
    #                           on=relationship[0])
    #     return df
    # finally:
    #     session.close()

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

    # elif tableName == 'test':
    #     print('Here')
    #     session = SessionLocal()
    #     try:
    #         result = session.query(OperationType).order_by(OperationType.OperTypeID.asc()).all()
    #         data = []
    #         for item in result:
    #             # print(item.OperName)
    #             op_type_names = []
    #             for op_type in item.operations:
    #                 if op_type.Операция:
    #                     op_type_names.append(op_type.Операция)
    #                 else:
    #                     op_type_names.append('')
    #             # print(op_type_names)
    #             # return
    #             data.append({
    #                 'OperTypeID': item.OperTypeID,
    #                 'OperName': item.OperName,
    #                 'ОперацииТип': ', '.join(op_type_names) if op_type_names != [] else ''
    #             })
    #         df = pd.DataFrame(data)
    #         return df
    #     except Exception as e:
    #         print(f"Error fetching data from database: {e}")
    #         # return fetchDataFromDb(tableName)
    #     finally:
    #         session.close()


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
            # return fetchDataFromDb(tableName)
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
