import sqlite3
import pandas as pd
import databasefunctions

conn = sqlite3.connect('lahmansbaseballdb.sqlite')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

# batting = pd.read_sql_query("SELECT * FROM batting WHERE yearID = 2017 AND AB > 0", conn)
# print("\n")
# print(batting)

teams = pd.read_sql_query("SELECT * FROM teams WHERE yearID IS 2017", conn)
teamsmall = teams["teamID"]
print(teamssmall)

teamsmall.insert(2, "ABs")


c.close()
