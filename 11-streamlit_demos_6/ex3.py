import streamlit as st
def process():
    print("Form submitted")

with st.form("login_form",clear_on_submit=True):
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    submitted=st.form_submit_button("Login",on_click=process)
