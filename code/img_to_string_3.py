from PIL import Image
from pytesseract import image_to_string


# print(image_to_string(Image.open('docs/imgs/address-fc.jpg')))

img_file = 'docs/imgs/address-fc_2.jpg'
data_from_img = image_to_string(Image.open(img_file))

outfile = "ocr_op/OCR-output_img-to-str_2.txt"
f = open(outfile, "a")

data_from_img = data_from_img.split()

append_start = False

for words in data_from_img:
    print(words.lower())
    if 'address' == words.lower() and not append_start:
        globals()['append_start'] = True

    if globals()['append_start']:
        f.write(words.lower() + ' ')

f.close()


print("Process completed. \nCheck ocr_op/OCR_output.txt file.")