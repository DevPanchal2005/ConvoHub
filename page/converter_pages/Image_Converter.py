import streamlit as st

from converters.image_converters.image_converter import ImageConverter

st.logo('resources/logo.png', size='large')

st.title('Image Converter')

# Allowed image formats
supported_formats = ["JPG", "JPEG", "PNG", "WEBP", "TIFF", "BMP", "ICO", "GIF", "PDF"]

# File uploader
input_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png", "webp", "tiff", "bmp", "ico", "gif"])

if input_file is not None:
    file_name = input_file.name
    file_ext = file_name.split('.')[-1].upper()

    # Remove current file type from the conversion options
    available_formats = [fmt for fmt in supported_formats if fmt != file_ext]

    if not available_formats:
        st.error("No available conversion formats.")
    else:
        # Select conversion format
        option = st.selectbox("Select image format to convert", available_formats, index=None, placeholder='Select an image format')

    if option is not None:
        output_image = ImageConverter.convert_image(input_file, option)

        file_name = file_name.replace(file_ext.lower(), option.lower())

        st.toast(f"Image successfully converted to {option} format.", icon="✅")
        
        st.download_button(
            label="Download Image",
            data=output_image,
            file_name=file_name,
            mime=f"image/{option.lower()}"
        )



