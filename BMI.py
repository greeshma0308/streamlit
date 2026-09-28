import streamlit as st
st.title("BMI")
weight=st.number_input("Weight in kg:",min_value=0)
height=st.number_input("Height in cm:",min_value=0)
btn=st.button("Calculate")
if btn:
    bmi=weight/((height/100)**2)
    st.write('BMI is:',bmi)
    if bmi<18.5:
        st.info("underweight")
    elif 18.5<=bmi<25:
        st.success("normal")
    elif 25<=bmi<30:
        st.warning("overweight")
    else:
        st.error("obesity")