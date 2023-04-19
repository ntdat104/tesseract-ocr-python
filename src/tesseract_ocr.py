import cv2
import os
import pytesseract
from PIL import Image
from progressbar import print_progress_bar

# Cấu hình tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ocr_images(images):
    finalText = ''

    for index ,image in enumerate(images):
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, image)
        text = pytesseract.image_to_string(Image.open(filename),lang='vie')
        os.remove(filename)
        finalText += text
        print_progress_bar(index, len(images), "OCR_IMAGES")

    return finalText