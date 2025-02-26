import streamlit as st

st.logo('resources/logo.png', size='large')

st.image('resources/image.png')

if st.button('Data Converter', icon='📊'):
    st.switch_page('page/converter_pages/Data_Converter.py')


    
