import streamlit as st
from model import get_response

st.title("🧠 Mental Health Chatbot - Registration")

# User Registration
st.subheader("Enter Your Name to Start Chatting")
username = st.text_input("Your Name")

if st.button("Start Chat"):
    if username:
        st.session_state["authenticated"] = True
        st.session_state["username"] = username
        st.success(f"Welcome, {username}! Start chatting below.")
    else:
        st.error("Please enter your name to continue.")

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
