import os
import subprocess
from typing import List
import pandas as pd
from QuoteEngine.QuoteModel import QuoteModel
from docx import Document


def read_csv_file(path):

    ls = []
    df = pd.read_csv(path)
    for row in df.iterrows():
        ls.append(QuoteModel(row[1][0], row[1][1]))
    return ls


def read_docx_file(path):
    with open(path, "r"):
        ls = []
        output = Document(path)
        for row in output.paragraphs:
            if len(row.text):
                splittedStr = row.text.split("-")
                ls.append(QuoteModel(splittedStr[0], splittedStr[1]))
        return ls


def read_text_file(path):
    with open(path, "r") as txtfile:
        ls = []
        output = txtfile.readlines()
        for row in output:
            splittedStr = row.split("-")
            if len(splittedStr) == 2:
                ls.append(QuoteModel(
                    splittedStr[0].strip(), splittedStr[1].strip()))
        return ls


def read_pdf_file(path: str) -> List[QuoteModel]:
    temp_file = r"./demo.txt"
    # Create a new demo.txt file if it doesn't exist yet
    with open(temp_file, 'w', encoding='utf-8') as f:
        pass

    # Convert the PDF file to plain text using pdftotext
    result = subprocess.run(
        ['pdftotext', '-layout', '-enc', 'UTF-8', path, temp_file], capture_output=True)
    # keeping this for debugging purposes
    if result.returncode != 0:
        print('Error converting PDF file:')
        print(result.stderr.decode('utf-8'))
        return []

    quotes = []

    with open(temp_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                parts = line.split(' - ')
                if len(parts) == 2:
                    quote = QuoteModel(parts[0], parts[1])
                    quotes.append(quote)
    os.remove(temp_file)
    return quotes
