import  streamlit as st
st.title("Subtraction")
num1=st.number_input("enter number 1:",min_value=0)
print(num1)
num2=st.number_input("enter number 2:",min_value=0)
print(num2)
btn=st.button("Subtract")
if btn: #if button is clicked
    result=num1-num2
    st.write("Difference is:",result) #shows it in the interface