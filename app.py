import streamlit as st

# Set page configuration
st.set_page_config(page_title="🧮 Interactive Calculator", page_icon="🧮", layout="wide")

# Title and introduction
st.title("🧮 Interactive Calculator")
st.write("Perform basic arithmetic operations with this calculator. Choose the operation and input two numbers.")

# Sidebar for selecting the operation
st.sidebar.title("🔧 Choose Operation")
operation = st.sidebar.selectbox(
    "Select the operation:",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Function to perform the calculation
def perform_calculation(op, a, b):
    if op == "Addition":
        return a + b
    elif op == "Subtraction":
        return a - b
    elif op == "Multiplication":
        return a * b
    elif op == "Division":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Calculate result
result = perform_calculation(operation, num1, num2)

# Display result
st.subheader("📈 Result:")
st.write(f"**Operation:** {operation}")
st.write(f"**Number 1:** {num1}")
st.write(f"**Number 2:** {num2}")
st.write(f"**Result:** {result}")

# Add some space and a footer
st.markdown("<br>", unsafe_allow_html=True)
st.write("Thank you for using the Interactive Calculator! 🚀")

