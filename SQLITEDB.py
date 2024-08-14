import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('student.db')

# Create a cursor object
cursor = conn.cursor()

# Create the STUDENT table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        CLASS TEXT NOT NULL,
        SECTION TEXT NOT NULL,
        Marks INTEGER
    )
''')

# Insert sample data into the STUDENT table
cursor.executemany('''
    INSERT INTO STUDENT (NAME, CLASS, SECTION, Marks)
    VALUES (?, ?, ?, ?)
''', [
    ("John Doe", "Data Science", "A", 85),
    ("Jane Smith", "Data Science", "B", 90),
    ("Jim Brown", "Computer Science", "A", 80),
    ("Lucy Gray", "Data Science", "A", 88),
    ("Tom Hanks", "Physics", "C", 75)
])

# Commit the transaction and close the connection
conn.commit()
conn.close()
