# Import necessary libraries
import streamlit as st

# Title of the app
st.title('Basic Streamlit App')

# Create a text input widget for the user to enter their name
name = st.text_input('Enter your name:')

# Display the greeting if the user has entered a name
if name:
    st.write(f'Hello, {name}! Welcome to Streamlit.')

# Add a slider widget for user to choose a number
number = st.slider('Choose a number', 0, 100, 50)

# Display the number selected by the user
st.write(f'You selected the number: {number}')
