import sqlite3

with sqlite3.connect('my_database.db') as conn:
    
    cursor = conn.cursor()

    # CREATE - Insert data
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    
    student_data = [('Shailesh', 23, 'shailesh@example.com'),('Meet', 23, 'meet@example.com')]
    conn.executemany(insert_query, student_data)
    
    # READ - Select all students
    select_query = 'SELECT * FROM Students;'
    cursor.execute(select_query)
    students = cursor.fetchall()
    print("All students:", students)
    
    # UPDATE - Update student data
    update_query = '''
    UPDATE Students 
    SET age = ?, email = ? 
    WHERE name = ?;
    '''
    update_data = (24, 'shailesh.new@example.com', 'Shailesh')
    cursor.execute(update_query, update_data)
    
    # DELETE - Delete a student
    delete_query = 'DELETE FROM Students WHERE name = ?;'
    cursor.execute(delete_query, ('Meet',))
    
    conn.commit()
    
    
