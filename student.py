import streamlit as st
from datetime import date
st.title("Student Registration Form")
name=st.text_input("Name")
age=st.number_input("Age",min_value=0)
dob=st.date_input("DOB",min_value=date(1990,1,1),max_value=date.today(),value=date(2000,1,1))
email=st.text_input("Email")
gender=st.radio("Gender",['Male','Female'])
courses=st.selectbox('Course',['Python','Java','dotnet','testing'])
btn=st.button("Register")
if btn:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"DOB: {dob}")
    st.write(f"Email: {email}")
    st.write(f"Gender: {gender}")
    st.write(f"Course: {courses}")

