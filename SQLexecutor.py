from sqlalchemy import text
from databaseconnect import engine

def execute_sql(sql):

    with engine.connect() as conn:

        result = conn.execute(text(sql))

        columns = list(result.keys())

        rows = result.fetchall()

        return columns, rows