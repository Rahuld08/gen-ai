import streamlit as st
def greetings(name):
    st.write("Good Evening ",name)
    
st.button("Press Me For Greetings",on_click=greetings,args=("Sachin",))