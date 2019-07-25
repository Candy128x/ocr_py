# Import libraries
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

PDF_file = "docs/doc1.pdf"

pages = convert_from_path(PDF_file, 500)
image_counter = 1

for page in pages:
    filename = "docs/imgs/page_" + str(image_counter) + ".jpg"
    page.save(filename, 'JPEG')
    image_counter = image_counter + 1

filelimit = image_counter - 1
outfile = "ocr_op/OCR_output.txt"
f = open(outfile, "a")

for i in range(1, filelimit + 1):
    filename = "docs/imgs/page_" + str(i) + ".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    f.write(text)

f.close()
print("Process completed. \nCheck ocr_op/OCR_output.txt file.")
