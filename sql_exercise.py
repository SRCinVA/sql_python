import sqlite3

def create_table():
    # create a connection and store it in a variable:
    conn=sqlite3.connect("lite.db")
    # create a cursor object
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)")   # the sql commands
    conn.commit()
    conn.close()

def insert(item, quantity, price): # let's populate it with an item
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))  # use single quotes on the insdie 
    conn.commit()
    conn.close()

insert("coffee cup", 10, 3)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")  # the SQL comamnds to query the DB
    rows=cur.fetchall() # get them
    conn.close() # close the connection
    return rows # present the rows

print(view()) # this prints out the output of view(), which are the returned rows

