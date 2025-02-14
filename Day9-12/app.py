import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.header('st.selectbox')
st.subheader('Day10')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.header('st.multiselect')
st.subheader('Day11')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

st.header('st.checkbox')
st.subheader('Day12')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

st.write('You ordered:', icecream, coffee, cola)

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
     
