import streamlit as st
import time
from model import get_response
from student_database import authenticate_student

# Set page title
st.set_page_config(page_title="🧠 Student Chatbot", layout="centered")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# **Login Page**
if not st.session_state.authenticated:
    st.title("🔐 Student Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if authenticate_student(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login successful! Redirecting to chatbot...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("❌ Invalid username or password!")

    st.stop()  # Prevent showing chatbot unless logged in

# **Chatbot Page (only after login)**
st.title("🧠 Student Chatbot")

# Sidebar info
with st.sidebar:
    st.header("About the Chatbot")
    st.write(f"👤 Logged in as **{st.session_state.username}**")
    st.write("🤖 This chatbot provides student-related support.")
    
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
if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        bot_response_placeholder = st.empty()
        time.sleep(1)  # Simulate thinking delay
        bot_response = get_response(prompt)
        bot_response_placeholder.markdown(bot_response)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
