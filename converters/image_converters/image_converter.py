from PIL import Image
from io import BytesIO

class ImageConverter:
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
