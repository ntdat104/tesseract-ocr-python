import cv2
import os
import pytesseract
from PIL import Image

# Cấu hình tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ocr_images(images):
    finalText = ''
    for image in images:
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, image)
        text = pytesseract.image_to_string(Image.open(filename),lang='vie')
        os.remove(filename)
        finalText += text
    return finalText