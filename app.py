import streamlit as st
from model import get_response

st.title("🧠 Mental Health Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("How are you feeling today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get bot response
    response = get_response(prompt)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})