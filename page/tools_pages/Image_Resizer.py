import streamlit as st
from PIL import Image
import io

st.logo('resources/logo.png', size='large')

st.title('Image Resizer')


st.write("This tool allows you to resize images to a specific width and height.")

uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True, caption="Original Image")
    st.write("Original Image Size:", img.width, "x", img.height)

    image_name = uploaded_file.name
    image_format = uploaded_file.type.split('/')[1].upper()

    maintain_aspect_ratio = st.checkbox("Maintain aspect ratio")

    width = st.number_input("Enter the desired width", min_value=100, max_value=5000, value=300, step=5)
    height = st.number_input("Enter the desired height", min_value=100, max_value=5000, value=300, step=5, disabled=maintain_aspect_ratio)

    # Resize logic
    if width and (not maintain_aspect_ratio or height):
        if maintain_aspect_ratio:
            height = int((width / img.width) * img.height)  # Calculate height automatically

        img = img.resize((width, height))
        st.image(img, caption="Resized Image")
        st.write("Resized Image Size:", img.width, "x", img.height)

        # Convert Image to Bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format=image_format)  
        img_bytes.seek(0)

        # Download button
        st.download_button(
            label="Click here to download the resized image",
            data=img_bytes,
            file_name=image_name,
            mime=uploaded_file.type
        )