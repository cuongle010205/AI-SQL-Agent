from databaseconnect import engine
from sqlalchemy import inspect
import streamlit as st

inspector = inspect(engine)
@st.cache_data
def get_schema():
    schema = ""

    for table in inspector.get_table_names():

        schema += f"\nTable: {table}\n"

        columns = inspector.get_columns(table)

        for col in columns:

            schema += f"- {col['name']} ({col['type']})\n"

    return schema
