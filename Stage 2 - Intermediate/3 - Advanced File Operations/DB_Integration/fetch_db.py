import sqlite3

with sqlite3.connect("my_database.db") as conn:
    # fetch as dict
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = "SELECT * FROM Students;"
    
    cursor.execute(query)
    
    # default ;- tuple of records 
    # print(cursor.fetchone())
    # print(cursor.fetchmany(1))
    # print(cursor.fetchall())
    
   
    # as dict
    for row in cursor.fetchall():
        print(dict(row))    