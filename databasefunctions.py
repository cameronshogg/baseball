import sqlite3
import pandas as pd

def newbatting(year): #This function pulls the batting database for all players with over 0 ABs in a year
    conn = sqlite3.connect('lahmansbaseballdb.sqlite')
    c = conn.cursor()
    sql = """SELECT * from batting where AB > ? AND yearID = ?"""
    AB = "0"
    year = str(year)
    batting = pd.read_sql_query(sql, conn, params = (AB, year))
    c.close()
    return batting

def teamsbuilder(batting): #This function connects to the database to create a new DF with the teamname and some stats
    conn = sqlite3.connect('lahmansbaseballdb.sqlite')
    c = conn.cursor()
    return

#def statline(teamname): #This function 
    
    
