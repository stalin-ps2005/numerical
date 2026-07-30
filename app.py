import streamlit as st

st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

symbol = st.selectbox(
    "Choose an operation",
    ["+", "-", "*"]
)

# Function
def calculate(num1, num2, symbol):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    else:
        return "Invalid symbol"

# Button
if st.button("Calculate"):
    result = calculate(num1, num2, symbol)
    st.success(f"Result: {result}")
