import  streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Add new book record")
title=st.text_input("Title")
author=st.text_input("Author")
price=st.number_input("Price")
pages =st.number_input("Pages")
language=st.text_input("Language")
btn=st.button("Add")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,pages,language)
    st.success("Record created successfully")
