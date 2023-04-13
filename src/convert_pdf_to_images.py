from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path,500, poppler_path=r'C:\Program Files\poppler-23.01.0\Library\bin')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, img in enumerate(images):
        img.save(f"{output_folder}/page_{i + 1}.png", "PNG")

pdf_path = 'pdf/hpg.pdf'
output_folder = './images'
convert_pdf_to_images(pdf_path, output_folder)

# import module
# from pdf2image import convert_from_path


# # Store Pdf with convert_from_path function
# images = convert_from_path('./pdf/hpg.pdf', 500 ,poppler_path=r'C:\Program Files\poppler-23.01.0\Library\bin')

# output_folder = './images'
# for i in range(len(images)):

# 	# Save pages as images in the pdf
# 	# images[i].save('page'+ str(i) +'.jpg', 'JPEG')
#     images[i].save(f"{output_folder}/page_{i + 1}.png", "PNG")