import sqlite3

def create_table():
    # create a connection and store it in a variable:
    conn=sqlite3.connect("lite.db")
    # create a cursor object
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)")   # the sql commands
    conn.commit()
    conn.close()

def insert(): # let's populate it with an item
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES ('wine glass', 8, 10.5)")  # use single quotes on the insdie 
    conn.commit()
    conn.close()