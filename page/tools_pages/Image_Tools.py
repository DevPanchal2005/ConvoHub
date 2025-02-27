import streamlit as st
from PIL import Image

st.logo('resources/logo.png', size='large')

st.title('Image Resizer')

st.write('This tool allows you to resize images to a specific width and height.')

uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:

    img = Image.open(uploaded_file)

    st.image(img, use_container_width=True, caption="Original Image")

    st.write("Original Image Size:", img.width, "x", img.height)

    maintain_aspect_ratio = st.checkbox("Maintain aspect ratio")

    width = st.number_input("Enter the desired width", min_value=100, max_value=5000, value=None, step=5)

    height = st.number_input("Enter the desired height", min_value=100, max_value=5000, value=None, step=5, disabled=maintain_aspect_ratio)
