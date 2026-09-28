import  streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Read a specific record")
id=st.number_input("ID",min_value=0)
btn=st.button("Retrieve")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(id)
    if record:
        st.write("Title:",record[1])
        st.write("Author:",record[2])
        st.write("Price:", record[3])
        st.write("Page:", record[4])
        st.write("Language:", record[5])
    else:
        st.error("No record found")