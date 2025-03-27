import sqlite3
import bcrypt

# Database connection
def connect_db():
    return sqlite3.connect("users.db", check_same_thread=False)

# Create users table (run once)
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)''')
    conn.commit()
    conn.close()

# Register a new user
def register_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Hash password before storing
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists

# Validate login
def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    
    if result:
        stored_password = result[0]
        if bcrypt.checkpw(password.encode(), stored_password):
            return True
    
    return False
