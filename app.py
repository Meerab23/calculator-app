import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Function to perform calculations
def calculate():
    num1 = st.number_input("Enter first number", step=1.0)
    num2 = st.number_input("Enter second number", step=1.0)

    operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"

    st.write(f"Result: {result}")

# Display the calculator
calculate()
