import streamlit as st
def printdetails(name,age):
    st.write(f"{name},{age}")
    
st.button("Press Me For Details",on_click=printdetails,kwargs={"name":"Sachin","age":45})