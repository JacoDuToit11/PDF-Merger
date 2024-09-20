from pypdf import PdfMerger
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(pdfs, output_file):
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()


def select_pdf_files():
    root = tk.Tk()
    root.withdraw()  

    file_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")],
    )

    return list(file_paths)

def merge_selected_pdfs():
    selected_pdfs = select_pdf_files()
    if not selected_pdfs:
        print("No files selected. Exiting.")
        return

    output_file = filedialog.asksaveasfilename(
        title="Save merged PDF as",
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    if not output_file:
        print("No output file specified. Exiting.")
        return

    merge_pdfs(selected_pdfs, output_file)
    print(f"Merged PDF saved as: {output_file}")


if __name__ == "__main__":
    merge_selected_pdfs()