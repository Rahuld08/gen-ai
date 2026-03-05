import streamlit as st

skills=["Java","C","Python","AI"]
st.write(skills)

person={"age":25,"name":"Satish"}
st.write(person)

class Student:
    def __init__(roll,name):
        self.roll=roll
        self.name=name

s=Student(101,"Piyush")
st.write(s)