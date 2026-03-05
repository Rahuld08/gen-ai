import streamlit as st
def add(a,b):
    st.session_state.sum=a+b
    
st.button("Add Numbers",on_click=add,args=(10,20))
st.write(st.session_state.get("sum","No sum yet")) 