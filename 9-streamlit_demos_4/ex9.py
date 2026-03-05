import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0


st.button("Press Me",on_click=lambda: st.session_state.__setitem__("count",st.session_state.count+1))
st.write("count:",st.session_state.count)