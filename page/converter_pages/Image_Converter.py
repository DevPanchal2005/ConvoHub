import streamlit as st

from converters.image_converters.image_converter import ImageConverter

st.logo('resources/logo.png', size='large')

input_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png", "webp"])

if input_file is not None:
    file_name = input_file.name
    file_type = input_file.type

    st.write(f"File Name: {file_name}")
    st.write(f"File Type: {file_type}")

    option = st.selectbox(
        "Select image type to convert", 
        ("JPG", "JPEG", "PNG", "WEBP", "TIFF", "BMP", "ICO", "GIF", "SVG", "PDF")
    )

    # match(file_type):

    #     case 'image/jpeg':
    #         if st.button('Convert to PNG', icon=':material/file_png:', use_container_width=True):
    #             file_name = file_name.replace('.jpeg', '.png')
    #             file_name = file_name.replace('.jpg', '.png')
    #             output_file = ImageConverter.jpeg_to_png(input_file)
    #             st.download_button("Download PNG", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="image/png")
    #             st.toast(f'{file_name} is ready to Download', icon='✅')

    #         if st.button('Convert to WEBP', icon=':material/image:', use_container_width=True):
    #             file_name = file_name.replace('.jpeg', '.webp')
    #             file_name = file_name.replace('.jpg', '.webp')
    #             output_file = ImageConverter.jpeg_to_webp(input_file)
    #             st.download_button("Download WEBP", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="image/webp")
    #             st.toast(f'{file_name} is ready to Download', icon='✅')

    #     case 'image/png':
    #         if st.button('Convert to JPEG', icon=':material/image:', use_container_width=True):
    #             file_name = file_name.replace('.png', '.jpeg')
    #             output_file = ImageConverter.png_to_jpeg(input_file)
    #             st.download_button("Download JPEG", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="image/jpeg")
    #             st.toast(f'{file_name} is ready to Download', icon='✅')

    #         if st.button('Convert to WEBP', icon=':material/image:', use_container_width=True):
    #             file_name = file_name.replace('.png', '.webp')
    #             output_file = ImageConverter.png_to_webp(input_file)
    #             st.download_button("Download WEBP", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="image/webp")
    #             st.toast(f'{file_name} is ready to Download', icon='✅')

    #     case 'image/webp':
    #         if st.button('Convert to JPEG', icon=':material/image:', use_container_width=True):
    #             file_name = file_name.replace('.webp', '.jpeg')
    #             output_file = ImageConverter.webp_to_jpeg(input_file)
    #             st.download_button("Download JPEG", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="image/jpeg")
    #             st.toast(f'{file_name} is ready to Download', icon='✅')

    #         if st.button('Convert to PNG', icon=':material/file_png:', use_container_width=True):
    #             file_name = file_name.replace('.webp', '.png')
    #             output_file = ImageConverter.webp_to_png(input_file)
    #             st.download_button("Download PNG", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="image/png")
    #             st.toast(f'{file_name} is ready to Download', icon='✅')
                
    #     case _:
    #         st.error("Invalid file type. Please upload a jpg/jpeg/png/webp image file.")


