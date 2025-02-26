from PIL import Image
from io import BytesIO

class ImageConverter:
    # # * Convert JPEG to PNG
    # @staticmethod
    # def jpeg_to_png(input_file):
    #     return ImageConverter.convert(input_file, 'PNG')
    
    # # * Convert JPEG to WEBP
    # @staticmethod
    # def jpeg_to_webp(input_file):
    #     return ImageConverter.convert(input_file, 'WEBP')

    # # * Convert PNG to JPEG
    # @staticmethod
    # def png_to_jpeg(input_file):
    #     return ImageConverter.convert(input_file, 'JPEG')
    
    # # * Convert PNG to WEBP
    # @staticmethod
    # def png_to_webp(input_file):
    #     return ImageConverter.convert(input_file, 'WEBP')

    # # * Convert WEBP to JPEG
    # @staticmethod
    # def webp_to_jpeg(input_file):
    #     return ImageConverter.convert(input_file, 'JPEG')

    # # * Convert WEBP to PNG
    # @staticmethod
    # def webp_to_png(input_file):
    #     return ImageConverter.convert(input_file, 'PNG')

    # * Generalized Convert Method
    @staticmethod
    def convert(input_file, output_format):
        buffer = BytesIO()
        img = Image.open(input_file)

        # Ensure RGB mode when converting to JPEG
        if output_format.upper() == 'JPEG':
            img = img.convert('RGB')
        
        img.save(buffer, format=output_format.upper())
        buffer.seek(0)
        return buffer
