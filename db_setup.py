import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("data/sales.csv")

print("CSV loaded ✅")

# Connect DB
conn = sqlite3.connect("sales.db")

# Create table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Table created ✅")

conn.close()