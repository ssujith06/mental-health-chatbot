import streamlit as st
import sqlite3
import bcrypt
from model import get_response

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user and bcrypt.checkpw(password.encode(), user[0]):
        return True
    return False

# Initialize database
init_db()

# Streamlit UI
st.title("🧠 Mental Health Chatbot - Login/Register")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Create an Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if register_user(new_user, new_password):
            st.success("Account created successfully! Please login.")
        else:
            st.error("Username already exists. Try a different one.")

elif choice == "Login":
    st.subheader("Login to Chat")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Login successful! Start chatting.")
        else:
            st.error("Invalid username or password.")

# Chatbot interface
if st.session_state.get("authenticated", False):
    st.title("🧠 Mental Health Chatbot")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("How are you feeling today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
