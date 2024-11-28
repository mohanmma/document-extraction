from pdf2image import convert_from_bytes
from PIL import Image
from io import BytesIO

def convert_file_to_png(file_content):
    # Convert PDF bytes to images
    images = convert_from_bytes(file_content)
    
    # Create a new blank image with the combined height of all pages
    final_image = Image.new("RGB", (images[0].width, sum(img.height for img in images)))
    
    # Paste each page image into the final image
    y_offset = 0
    for img in images:
        final_image.paste(img, (0, y_offset))
        y_offset += img.height
    
    # Save the final image to a byte array
    png_byte_array = BytesIO()
    final_image.save(png_byte_array, format='PNG')
    
    return png_byte_array.getvalue()
