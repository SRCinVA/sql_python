import sqlite3

# create a connection and store it in a variable:
conn=sqlite3.connect("lite.db")
# create a cursor object
cur=conn.cursor()
cur.execute("CREATE TABLE store (item TEXT, quantity INT, price REAL)")   # your sql commands