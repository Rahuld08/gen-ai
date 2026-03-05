import streamlit as st
def add(a,b):
    st.session_state.sum=a+b
    
fno=st.number_input("Enter first no",step=1)
sno=st.number_input("Enter secnd no",step=1)
st.button("Add Numbers",on_click=add,args=(fno,sno))
st.write(st.session_state.get("sum","No sum yet")) 