import sqlite3
import pandas as pd

data = pd.read_csv("clean_fuse_data.csv")
conn = sqlite3.connect("fuse_data.db")

data.to_sql("fuses", conn, if_exists = "replace", index = False)
cursor = conn.cursor()
cursor.execute("SELECT k, current, time_taken_to_blow FROM fuses ORDER BY time_taken_to_blow ASC LIMIT 5")

results = cursor.fetchall()

for row in results:
    print(row)

conn.close()