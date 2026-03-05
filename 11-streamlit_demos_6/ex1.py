import streamlit as st
print("run")
with st.form("login_form"):
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    submitted=st.form_submit_button("Login")
if submitted:
    if not username or not password:
        st.error("All fields required!")
    else:
        st.success("Login successfull")