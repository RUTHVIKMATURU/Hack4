import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect('elearning.db')
cursor = conn.cursor()

# Fetch all courses
cursor.execute("SELECT * FROM courses")
courses = cursor.fetchall()

# Print all courses
print("Courses:")
for course in courses:
    print(course)

# Close the connection
conn.close()
