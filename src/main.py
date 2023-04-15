from converter import convert_pdf_to_images
from converter import convert_string_to_raw_metadata
from converter import convert_string_to_metadata
from loader import load_images_from_folder
from tesseract_ocr import ocr_images

# Khai báo các path
pdf_path = 'pdf/bctc.pdf'
output_folder = 'images'

# Chuyển đổi pdf -> images
convert_pdf_to_images(pdf_path, output_folder)

# Lấy toàn bộ ảnh trong thư mục
images = load_images_from_folder(output_folder)

# Sử dụng tesseract_ocr để tiến hành trích xuất text từ ảnh
text = ocr_images(images)

# Chuyển đổi text -> raw_metadata
raw_metadata = convert_string_to_raw_metadata(text)

# Chuyển đổi text -> metadata
metadata = convert_string_to_metadata(text)

# Hiển thị kết quả
print(text)
print(raw_metadata)
print(metadata)