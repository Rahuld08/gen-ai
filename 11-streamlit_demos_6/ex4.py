import streamlit as st
def process():
    if not st.session_state.username or not st.session_state.password:
        st.error("All fields required")
    else:
        st.success("Form submitted")

with st.form("login_form",clear_on_submit=True):
    username=st.text_input("Username",key="username")
    password=st.text_input("Password",type="password",key="password")
    submitted=st.form_submit_button("Login",on_click=process)
