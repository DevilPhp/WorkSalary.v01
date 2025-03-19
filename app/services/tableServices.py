import pandas as pd
from app.database import engine
from sqlalchemy.orm import joinedload
from app.database import SessionLocal
from app.database.workers import WorkerPosition, OperationType


def fetchDataFromDb(tableName):
    """ Fetches data from PostgreSQL table """
    with engine.connect() as conn:
        df = pd.read_sql(f'SELECT * FROM "{tableName}";', conn)
    return df


def fetchDataFromDbWithRelations(tableName, relationships=None):
    """ Fetches data from PostgreSQL table with related data """
    session = SessionLocal()
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

    if tableName == 'workerPositions':
        workers = session.query(WorkerPosition).order_by(WorkerPosition.ДлъжностКод.asc()).all()
        print(workers)  # This will print the SQL query executed by SQLAlchemy.
        return

        query = session.query(WorkerPosition).options(joinedload(WorkerPosition.operationTypes))
        result = query.all()

        print(result)  # This will print the SQL query executed by SQLAlchemy.

        data = []
        for item in result:
            data.append({
                'id': item.id,
                'ДлъжностКод': item.ДлъжностКод,
                'Длъжност': item.Длъжност,
                'Коефициент': item.Коефициент,
                'ВидОперация': item.operationTypes.OperName if item.operationTypes else ''
            })

        df = pd.DataFrame(data)
        session.close()
        return df
    else:
        return fetchDataFromDb(tableName)
