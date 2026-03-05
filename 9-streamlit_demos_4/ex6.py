import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0
clicked=st.button("Press Me")
if clicked:
    st.session_state.count+=1
st.write("count:",st.session_state.count)