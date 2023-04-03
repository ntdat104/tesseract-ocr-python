import tabula

def extract_tables_from_pdf(pdf_path, output_format="dataframe"):
    # If output_format is "dataframe", the function will return a list of pandas DataFrames
    # Otherwise, it will return a list of strings in the specified format (csv, tsv, or json)
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, output_format=output_format)

    return tables

pdf_path = '../pdf/Bao_cao_tai_chinh_Hop_nhat_Kiem_toan_nam_2022.pdf'
tables = extract_tables_from_pdf(pdf_path)

# Process the tables
for i, table in enumerate(tables):
    print(f"Table {i + 1}:")
    print(table)
    print("\n")