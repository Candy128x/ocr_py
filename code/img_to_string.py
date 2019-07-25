from PIL import Image
from pytesseract import image_to_string


print(image_to_string(Image.open('docs/imgs/page_1.jpg')))