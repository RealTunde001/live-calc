import streamlit as st
from PIL import Image

st.title("Calculator App")

def add(x,y):
    z = x+y
    return z

def sub(x,y):
    z = x-y
    return z

def mul(x,y):
    z = x*y
    return z



def calc():
    if operation == "addition":
       return add(x,y)
    elif operation == "subtraction":
        return sub(x,y)
    else:
        return mul(x,y)
    
col1, col2 = st.columns(2)

with col1:

 x = st.number_input("Input your first number")
 y= st.number_input("input your second number")

with col2:
 if st.button("Add"):
    st.write(add(x,y))

  
 if st.button("substract"):
    st.write(sub(x,y))
    
 if st.button("multiply"):
    st.write(mul(x,y))