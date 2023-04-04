from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, img in enumerate(images):
        img.save(f"{output_folder}/page_{i + 1}.png", "PNG")

pdf_path = '../pdf/hpg.pdf'
output_folder = './images'
convert_pdf_to_images(pdf_path, output_folder)