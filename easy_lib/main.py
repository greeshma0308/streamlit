import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','VIEW','RETRIEVE','UPDATE','DELETE'])
b=BookListCreateRetrieveUpdateDelete()
with tab1:
    st.title("ADD")
with tab2:
    st.title("VIEW")
with tab3:
    st.title("RETRIEVE")
with tab4:
    st.title("UPDATE")
with tab5:
    st.title("DELETE")