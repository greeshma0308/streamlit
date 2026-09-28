import streamlit as st
name=st.text_input("Enter name")
age=st.number_input("Enter age")
place=st.text_input("Enter place")
gender=st.radio("Select gender",['Male','Female'])
qualification=st.selectbox('Select qualification',['BBA','BCA','BTECH'])
btn=st.button("Submit")
if btn:
    st.title("USER INFO")
    st.subheader(f"Name: {name}")
    st.subheader(f"Age: {age}")
    st.subheader("Place:", place)
    st.subheader('Gender:',gender)
    st.subheader('Qualification:',qualification)
