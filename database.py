import sqlite3
conn = sqlite3.connect('lahmansbaseballdb.sqlite')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
c.close()
