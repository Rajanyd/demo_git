import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, pages_per_file=4):

    base_name = os.path.splitext(os.path.basename(input_pdf))[0]

    output_dir = f"{base_name}_split"
    os.makedirs(output_dir, exist_ok=True)

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    print(f"Total Pages: {total_pages}")

    for start in range(0, total_pages, pages_per_file):

        writer = PdfWriter()

        end = min(start + pages_per_file, total_pages)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_filename = f"{base_name}_{start + 1}-{end}.pdf"

        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_filename}")

# ===== PDF NAME =====
input_pdf_path = "YOUR_FILE_NAME.pdf"

split_pdf(input_pdf_path, pages_per_file=4)