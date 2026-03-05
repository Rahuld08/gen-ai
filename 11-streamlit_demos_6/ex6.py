import streamlit as st
from datetime import date,time
st.title("📅Booking Form")
start_time=time(10,0)
end_time=time(18,0)
with st.form("booking_form"):
    name=st.text_input("Enter your name")
    service=st.selectbox("Select service",["Haircut","Facial","Massage"])
    booking_date=st.date_input("Select date",min_value=date.today())
    booking_time=st.time_input("Select time",value=start_time)
    agree=st.checkbox("I agree to the terms")
    submit=st.form_submit_button("Book Now")
if submit:
    errors=[]
    if not name.strip():
        errors.append("❌ Name is required")
    if booking_time <start_time or booking_time >end_time:
        errors.append("❌ Time must be between 10 to 6")
    if not agree:
        errors.append("❌ You must agree to conditions")
    if errors:
        for err in errors:
            st.error(err)
    else:
        st.success("✅ Booking Confirmed")
        st.write("**Name**",name)
        st.write("**Service**",service)
        st.write("**Date**",booking_date)
        st.write("**Time**",booking_time)
        