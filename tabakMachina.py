import streamlit as st
import numpy as np

st.title("Tabak Machina")
# Sidebar inputs
st.sidebar.header("Matrix Parameters")
num_values = st.sidebar.number_input("Number of values to add", min_value=1, max_value=100, value=10)
min_value = st.sidebar.number_input("Minimum value", value=1)
max_value = st.sidebar.number_input("Maximum value", value=100)

# Generate matrix on button click
if st.sidebar.button("Generate Matrix"):
    # Create a 10x10 matrix of zeros
    matrix = np.zeros((10, 10))
    
    # Randomly add 'num_values' values to random positions in the matrix
    for _ in range(num_values):
        row = np.random.randint(0, 10)
        col = np.random.randint(0, 10)
        matrix[row, col] = np.random.randint(min_value, max_value)
    
    # Display the matrix
    st.write("Generated Matrix:")
    st.write(matrix)
    
    # Find and display the maximum value in the matrix
    max_matrix_value = np.max(matrix)
    st.write(f"Maximum matrix value: {max_matrix_value}")
