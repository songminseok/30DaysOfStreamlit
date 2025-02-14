import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write('I’m ', age, ' years old.')

st.subheader('Range Slider')

value = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', value)

st.subheader('Range time slider')

appointment = st.slider(
    'Schedule your appointment:',
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')

start_time = st.slider(
    'When do you start?',
    value=(datetime(2021, 1, 1, 9, 30), datetime(2022, 1, 1, 12, 0)),
    format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("My favorite color is", color)