import streamlit as st

st.set_page_config(page_title='Day19', page_icon=':sunglasses:', layout='wide')

st.title('How to layout a Streamlit app')

with st.expander('About this app'):
    st.write('This app demonstrates how to layout a Streamlit app')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.title('Sidebar')
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['❤️', '🎉', '😄', '🍉'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['Pizza', 'Burger', 'Pasta', 'Salad'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')