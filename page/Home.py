import streamlit as st

st.logo('resources/logo.png', size='large')

st.image('resources/image.png')

with st.container(border=True):
    "## 🤔 What is ConvoHub?"

    """
    - ConvoHub is a web application that provides various tools and converters for data and image processing.  

    - It is a one-stop solution for all your data and image processing needs. 

    - It provides a user-friendly interface that makes it easy to use.

    - It is a completely free and open-source project.

    - All the computations are done on the client-side, so your data is safe and secure.
    """

with st.container(border=True):
    "## Why is Data Converter Required?"
    """
    - Data Converter converts your data from one format to another formats such as CSV, Excel, JSON, PDF, HTML, TSV with just few clicks.
    """
    st.page_link("page/converter_pages/Data_Converter.py", label="Data Converter",  icon='📊', use_container_width=True)

with st.container(border=True):
    "## Why is Image Converter Required?"
    """
    - Image Converter converts your image from one format to another formats such as JPG, PNG, BMP, TIFF, GIF with just few clicks.
    """
    st.page_link("page/converter_pages/Image_Converter.py", label="Image Converter", icon='🖼️', use_container_width=True)

with st.container(border=True):
    "## Why is Image Resizer Needed?"
    """
    - In the era, where social media platforms have specific image size requirements, Image Resizer helps you resize your image to the required size.
    """
    st.page_link("page/tools_pages/Image_Resizer.py", label="Image Resizer", icon='📏', use_container_width=True)

with st.container(border=True):
    "## You seem interested, Want to know more?"
    """
    - Want to know more about ConvoHub and the technologies used in it?
    """
    st.page_link("page/About_Us.py", label="About Us", icon='👨‍💻', use_container_width=True)
