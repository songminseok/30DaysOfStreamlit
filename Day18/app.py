import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Upload a CSV file')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Summary statistics')
    st.write(df.describe())
else:
    st.info('Upload a CSV file')