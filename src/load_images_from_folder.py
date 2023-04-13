import cv2
import os
import pytesseract
from PIL import Image

# Cấu hình tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Đọc nhiều ảnh từ folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        # Đọc ảnh
        img = cv2.imread(os.path.join(folder,filename))

        # Chuyển ảnh BGR -> ảnh Xám (dạng binary)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Dùng threshold để giảm độ nhiễu và tăng độ chính xác khi chuẩn đoán
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        if img is not None:
            images.append(img)

    return images

def ocr_images(images):
    finalText = ''
    for image in images:
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, image)
        text = pytesseract.image_to_string(Image.open(filename),lang='vie')
        os.remove(filename)
        finalText += text
    return finalText

images = load_images_from_folder('images')
print(ocr_images(images))

# for image in images:
#     text = pytesseract.image_to_string(Image.open(image),lang='vie')
#     print(text)