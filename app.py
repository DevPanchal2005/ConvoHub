import streamlit as st

home = st.Page("page/Home.py", icon='🏠')

"hello World"

data_converter = st.Page("page/converter_pages/Data_Converter.py", icon='📊')
image_converter = st.Page("page/converter_pages/Image_Converter.py", icon='🖼️')

pg = st.navigation(
    {
        "Home": [home],
        "Converters": [data_converter, image_converter],
        "Tools": []
    }
)
pg.run()