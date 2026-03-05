import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0

def increment():
     st.session_state.count+=1

st.button("Press Me",on_click=increment)
st.write("count:",st.session_state.count)