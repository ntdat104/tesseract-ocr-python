from pdf2image import convert_from_path
import os
import json

def convert_string_to_raw_metadata(text):
    metadata = {}
    for i in range(len(text.split("\n"))):
        metadata[i] = text.split("\n")[i]
    with open("raw_metadata.json", "w", encoding='utf-8') as outfile:
        json.dump(metadata, outfile, ensure_ascii=False)
    return metadata

def convert_string_to_metadata(text):
    metadata = {}
    for i in text.split("\n"):
        for j in range(100, 440):
            if (" " + str(j) + " ") in i:
                metadata[j] = i
    with open("metadata.json", "w", encoding='utf-8') as outfile:
        json.dump(metadata, outfile, ensure_ascii=False)
    return metadata

def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path,500, poppler_path=r'C:\Program Files\poppler-23.01.0\Library\bin')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, img in enumerate(images):
        img.save(f"{output_folder}/page_{i + 1}.png", "PNG")