import  streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Update book record")
id=st.number_input("ID",min_value=0)
title=st.text_input("Title")
author=st.text_input("Author")
price=st.number_input("Price",min_value=0)
pages =st.number_input("Pages",min_value=0)
language=st.text_input("Language")
btn=st.button("Update")
if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record=b.update(id,title, author, price, pages, language)
    if record:
        st.success("Updated successfully")
    else:
        st.error("No record found")
