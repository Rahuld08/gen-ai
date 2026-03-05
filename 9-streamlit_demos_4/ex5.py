import streamlit as st
st.text_input("Enter your name:",key="name")
if st.session_state.name:
        st.write("Hello",st.session_state.name)
    