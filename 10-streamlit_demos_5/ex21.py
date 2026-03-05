import streamlit as st

st.title("💬 Chat App")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])  
        


user_msg=st.chat_input("Type your message")

if user_msg:
    st.session_state.messages.append({"role":"user","content":user_msg})
    st.session_state.messages.append({"role":"assistant","content":f"Echo:{user_msg}"})
    st.rerun()
