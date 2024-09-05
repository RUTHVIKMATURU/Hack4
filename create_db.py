import sqlite3

# Connect to SQLite Database (or create if it doesn't exist)
conn = sqlite3.connect('elearning.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    course_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    module_id INTEGER,
    FOREIGN KEY (module_id) REFERENCES modules (id)
);
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
