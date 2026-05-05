import sqlite3
import pandas as pd
from query_generator import generate_sql

def run_query(question):
    conn = sqlite3.connect("sales.db")

    df = pd.read_sql("SELECT * FROM sales", conn)
    columns = list(df.columns)

    sql_query = generate_sql(question, columns)

    try:
        result = pd.read_sql(sql_query, conn)
    except Exception as e:
        result = f"Error: {e}"

    conn.close()

    return sql_query, result