import pytesseract
import pdfplumber
from PIL import Image

def extract_vietnamese_text_from_pdf(pdf_path):
    pytesseract.pytesseract.tesseract_cmd = 'path/to/your/tesseract.exe'  # For Windows, set the path to the Tesseract executable
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)

        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            im = page.to_image(resolution=300)
            img = im.original

            page_text = pytesseract.image_to_string(img, lang='vie')  # Set the language to Vietnamese (vie)
            text += page_text + "\n"
    
    return text

pdf_path = '../pdf/Bao_cao_tai_chinh_Hop_nhat_Kiem_toan_nam_2022.pdf'
text = extract_vietnamese_text_from_pdf(pdf_path)
print(text)