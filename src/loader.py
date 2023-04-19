import cv2
import os
from progressbar import print_progress_bar

# Đọc nhiều ảnh từ folder
def load_images_from_folder(folder):
    images = []
    for index ,filename in enumerate(os.listdir(folder)):
        # Đọc ảnh
        img = cv2.imread(os.path.join(folder,filename))

        # Chuyển ảnh BGR -> ảnh Xám (dạng binary)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Dùng threshold để giảm độ nhiễu và tăng độ chính xác khi chuẩn đoán
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        if img is not None:
            images.append(img)
        print_progress_bar(index, len(os.listdir(folder)), "LOAD_IMAGES_FROM_FOLDER")

    return images