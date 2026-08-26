import sqlite3

with sqlite3.connect('my_database.db') as conn:
    
    cursor = conn.cursor()
    
    create_query = '''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT
        );
    '''
    
    cursor.execute(create_query)
    
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    
    # student_data = ('Shailesh', 23, 'shailesh@example.com')
    # conn.execute(insert_query,student_data)
    
    # insert many data 
    student_data = [('Shailesh', 23, 'shailesh@example.com'),('Meet', 23, 'meet@example.com')]
    conn.executemany(insert_query,student_data)
    

    