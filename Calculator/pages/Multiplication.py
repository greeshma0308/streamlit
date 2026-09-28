import  streamlit as st
st.title("Multiplication")
num1=st.number_input("enter number 1:",min_value=0)
print(num1)
num2=st.number_input("enter number 2:",min_value=0)
print(num2)
btn=st.button("Multiply")
if btn: #if button is clicked
    result=num1*num2
    st.write("Product:",result) #shows it in the interface