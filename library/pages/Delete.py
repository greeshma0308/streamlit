import  streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Delete book record")
id=st.number_input("ID",min_value=0)
btn=st.button("Delete")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.delete(id)
    if record:
        st.success("Deleted successfully")
    else:
        st.error("No record found")