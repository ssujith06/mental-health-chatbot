import streamlit as st
import time
from model import get_response
from database import create_table, register_user, authenticate_user

# Initialize DB table
create_table()

# Set page title
st.set_page_config(page_title="🧠 Mental Health Chatbot", layout="centered")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Function to switch between login & register pages
def switch_page():
    st.session_state.page = "register" if st.session_state.page == "login" else "login"

# Default page: login
if "page" not in st.session_state:
    st.session_state.page = "login"

# **Registration Page**
if st.session_state.page == "register":
    st.title("📝 Register to Access the Chatbot")
    
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    
    if st.button("Register"):
        if register_user(username, password):
            st.success("✅ Registration successful! Please login.")
            switch_page()
        else:
            st.error("⚠️ Username already exists!")

    st.button("Already have an account? Login", on_click=switch_page)
    st.stop()

# **Login Page**
if not st.session_state.authenticated:
    st.title("🔐 Login to Mental Health Chatbot")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password!")

    st.button("New user? Register", on_click=switch_page)
    st.stop()

# **Chatbot Page (only after login)**
st.title("🧠 Mental Health Chatbot")

# Sidebar info
with st.sidebar:
    st.header("About the Chatbot")
    st.write(f"👤 Logged in as **{st.session_state.username}**")
    st.write("🤖 This chatbot provides basic mental health support.")
    st.write("💡 It is not a replacement for professional help.")
    st.write("📞 If you need urgent help, reach out to a professional.")

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input handling
if prompt := st.chat_input("How are you feeling today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        bot_response_placeholder = st.empty()
        time.sleep(1)  # Simulate thinking delay
        bot_response = get_response(prompt)
        bot_response_placeholder.markdown(bot_response)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
