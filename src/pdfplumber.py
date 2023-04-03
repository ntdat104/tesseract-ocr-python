import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
        text = ""

        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            text += page.extract_text()
    
    return text

pdf_path = '../pdf/Bao_cao_tai_chinh_Hop_nhat_Kiem_toan_nam_2022.pdf'
text = extract_text_from_pdf(pdf_path)
print(text)