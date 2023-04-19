import os
import json
from pdf2image import convert_from_path
from progressbar import print_progress_bar

def convert_string_to_raw_metadata(text):
    metadata = {}
    for index, item in enumerate(text.split("\n")):
        metadata[index] = item
        print_progress_bar(index, len(text.split("\n")), "CONVERT_STRING_TO_RAW_METADATA")
    with open("raw_metadata.json", "w", encoding='utf-8') as outfile:
        json.dump(metadata, outfile, ensure_ascii=False)
    return metadata

def convert_string_to_metadata(text):
    metadata = {}
    for index, item in enumerate(text.split("\n")):
        for j in range(1, 440):
            if (" " + str(j) + " ") in item:
                metadata[j] = item
        print_progress_bar(index, len(text.split("\n")), "CONVERT_STRING_TO_METADATA")
    with open("metadata.json", "w", encoding='utf-8') as outfile:
        json.dump(metadata, outfile, ensure_ascii=False)
    return metadata

def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path,500, poppler_path=r'C:\Program Files\poppler-23.01.0\Library\bin')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, img in enumerate(images):
        img.save(f"{output_folder}/page_{index + 1}.png", "PNG")
        print_progress_bar(index, len(images), "CONVERT_PDF_TO_IMAGES")