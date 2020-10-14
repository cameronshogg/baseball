import sqlite3
import pandas as pd
import numpy as np
import matplotlib as plt
from databasefunctions import newbatting

conn = sqlite3.connect('lahmansbaseballdb.sqlite')
c = conn.cursor()

battingdata = newbatting(2017)

teamsdata = pd.read_sql_query("SELECT * FROM teams", conn)
teams = teamsdata[["teamID", "W", "L", "R",]]

c.close()


#This code shows the names of all the tables 
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())

# not even sure what this code does
# print(teams)
# teamsmall = teams[["teamID", "yearID"]]
# teamsmall["BA"] = np.nan
# teamsmall["sp_ERA"] = np.nan
# teamsmall["rp_ERA"] = np.nan
# print(teamsmall)

#This code shows the headers in a given table (tablename)
# import sqlite3
# conn = sqlite3.connect('lahmansbaseballdb.sqlite')
# c = conn.execute('select * from tablename')
# colnames = c.description
# for row in colnames:
#     print row[0]
