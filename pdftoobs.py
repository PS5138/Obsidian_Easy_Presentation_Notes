# this works through the command line!

import fitz  # PyMuPDF
import os
import argparse

def add_pdf_to_markdown(pdf_path, markdown_file):
    """
    Adds Obsidian-style links for each page of a PDF to a Markdown file.

    Args:
        pdf_path (str): Full path to the PDF file.
        markdown_file (str): Path to the Markdown file where links will be added.
    """
    # Extract the PDF file name from the full path
    pdf_file_name = os.path.basename(pdf_path)  # Extracts just the file name

    # Open the PDF file using the full path
    try:
        pdf_document = fitz.open(pdf_path)  # Use pdf_path to open the file
    except FileNotFoundError:
        print(f"Error: File not found - {pdf_path}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Get the total number of pages
    total_pages = pdf_document.page_count

    # Append to the Markdown file
    with open(markdown_file, "a") as md_file:
        md_file.write(f"\n# {pdf_file_name}\n")  # Add a header for the PDF
        for page in range(1, total_pages + 1):
            md_file.write(f"![[{pdf_file_name}#page={page}]]\n\n")  # Add a blank line after each link

    print(f"Added references for {pdf_file_name} to {markdown_file}.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Add Obsidian-style PDF links to a Markdown file.")
    parser.add_argument("pdf_path", help="Full path to the PDF file.")
    parser.add_argument("markdown_file", help="Path to the Markdown file.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the parsed arguments
    add_pdf_to_markdown(args.pdf_path, args.markdown_file)