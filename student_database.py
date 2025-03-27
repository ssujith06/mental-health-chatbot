import sqlite3
import bcrypt

# Connect to the database
def connect_db():
    return sqlite3.connect("students.db", check_same_thread=False)

# Create table and insert sample student data (Run this once)
def initialize_student_data():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)''')

    # Sample student data (hashed passwords)
    students = [
        ("student1", bcrypt.hashpw("pass123".encode(), bcrypt.gensalt())),
        ("student2", bcrypt.hashpw("mypassword".encode(), bcrypt.gensalt())),
        ("student3", bcrypt.hashpw("securepass".encode(), bcrypt.gensalt())),
    ]

    # Insert sample data
    for username, password in students:
        try:
            cursor.execute("INSERT INTO students (username, password) VALUES (?, ?)", (username, password))
        except sqlite3.IntegrityError:
            pass  # Ignore if user already exists

    conn.commit()
    conn.close()

# Check if student exists
def authenticate_student(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM students WHERE username=?", (username,))
    result = cursor.fetchone()
    
    if result and bcrypt.checkpw(password.encode(), result[0]):
        return True  # Login successful
    
    return False  # Login failed

# Run this once to initialize database with sample data
if __name__ == "__main__":
    initialize_student_data()
    print("Student database initialized!")
