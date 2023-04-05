import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        text = ""

        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    
    return text

pdf_path = '../pdf/Bao_cao_tai_chinh_Hop_nhat_Kiem_toan_nam_2022.pdf'
text = extract_text_from_pdf(pdf_path)
print(text)