import streamlit as st
with st.form("loginemail"):
    st.text_input("Email")
    st.form_submit_button("login")

with st.form("loginmobile"):
    st.text_input("Mobile")
    st.form_submit_button("login")

