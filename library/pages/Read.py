import  streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Read all records")
b=BookListCreateRetrieveUpdateDelete()
records=b.list()
st.table(records)