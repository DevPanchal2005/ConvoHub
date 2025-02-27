import streamlit as st

home = st.Page("page/Home.py", icon='🏠')

data_converter = st.Page("page/converter_pages/Data_Converter.py", icon='📊')
image_converter = st.Page("page/converter_pages/Image_Converter.py", icon='🖼️')

image_tools = st.Page("page/tools_pages/Image_Tools.py", icon='🛠️')

pg = st.navigation(
    {
        "Home": [home],
        "Converters": [data_converter, image_converter],
        "Tools": [image_tools]
    }
)
pg.run()