import streamlit as st

st.title("Internship Batch 2026 - Generative AI - Basic UI Code")

st.write("This is a basic UI code for the internship batch 2026 on Generative AI. You can customize this code according to your needs and requirements. This code is just a starting point for you to build your own UI for the internship batch 2026 on Generative AI.")

st.header('select a number')
number = st.slider('Select a number', 0, 50, 5)

st.subheader('Result: ')
square = number ** 2
st.write(f"The square of {number} is {square}.")