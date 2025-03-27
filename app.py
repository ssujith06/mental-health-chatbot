import streamlit as st
import time
from model import get_response

# Dummy user credentials (you can replace this with a database)
USER_CREDENTIALS = {"admin": "password123", "user": "chatbot123"}

# Set page title
st.set_page_config(page_title="🧠 Mental Health Chatbot", layout="centered")

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Function to check login credentials
def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.authenticated = True
        st.session_state.username = username
    else:
        st.error("Invalid username or password!")

# Login Page
if not st.session_state.authenticated:
    st.title("🔐 Login to Mental Health Chatbot")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)

    st.stop()  # Stop execution here if not logged in

# Chatbot Page (only accessible after login)
st.title("🧠 Mental Health Chatbot")

# Sidebar info
with st.sidebar:
    st.header("About the Chatbot")
    st.write(f"👤 Logged in as **{st.session_state.username}**")
    st.write("🤖 This chatbot provides basic mental health support.")
    st.write("💡 It is not a replacement for professional help.")
    st.write("📞 If you need urgent help, reach out to a professional.")
    
    # Logout button
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
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Show typing effect for bot response
    with st.chat_message("assistant"):
        bot_response_placeholder = st.empty()
        time.sleep(1)  # Simulate thinking delay
        bot_response = get_response(prompt)
        bot_response_placeholder.markdown(bot_response)

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
