import sqlite3
import pandas as pd

def newbatting(year):
    conn = sqlite3.connect('lahmansbaseballdb.sqlite')
    c = conn.cursor()
    batting = pd.read_sql_query("SELECT * FROM batting WHERE AB > 0 AND yearID =  ?", conn)
    c.close()
    return batting
