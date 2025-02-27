from PIL import Image
from io import BytesIO

class ImageConverter:
    # * Generalized Convert Method with Handling for Transparency, Animations, and PDF Conversion
    @staticmethod
    def convert_image(input_file, output_format):
        """
        Converts an image to the specified format with handling for transparency, animations, and PDF conversion.

        :param input_file: File-like object containing the image.
        :param output_format: Desired output format (e.g., "PNG", "JPEG", "GIF", "TIFF", "PDF").
        :return: A BytesIO buffer containing the converted image.
        """
        buffer = BytesIO()
        img = Image.open(input_file)
        output_format = output_format.upper()

        if output_format=="JPG":
            output_format = "JPEG"


        # Ensure RGB mode when converting images without native support for transparency
        if output_format in ["JPEG", "PDF"]:
            img = img.convert("RGB")  # PDF and JPEG do not support transparency

        # Preserve animations in GIFs
        save_params = {}
        if img.format == "GIF" and output_format == "GIF":
            save_params["save_all"] = True

        # Preserve transparency if converting from PNG/WebP to another format that supports it
        if "A" in img.getbands() and output_format in ["PNG", "TIFF", "WEBP"]:
            save_params["transparency"] = 0
        
        img.save(buffer, format=output_format, **save_params)
        buffer.seek(0)
        return buffer

