import sqlite3

def update_schema():
    conn = sqlite3.connect('elearning.db')
    cursor = conn.cursor()

    # Add new columns to the courses table
    cursor.execute("""
    ALTER TABLE courses
    ADD COLUMN textbook TEXT;
    """)
    
    cursor.execute("""
    ALTER TABLE courses
    ADD COLUMN reference_links TEXT;
    """)

    cursor.execute("""
    ALTER TABLE courses
    ADD COLUMN question_papers TEXT;
    """)
    cursor.execute("""
    ALTER TABLE courses
    ADD COLUMN textbook_file TEXT;
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_schema()
