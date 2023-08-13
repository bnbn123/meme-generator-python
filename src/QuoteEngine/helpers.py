import pandas as pd
from QuoteEngine.QuoteModel import QuoteModel
from docx import Document
import subprocess
import os


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


def read_pdf_file(path):
    TEMP_FILE = "demo.txt"
    with open(path, encoding="utf8"):
        subprocess.call(
            ['pdftotext', path, TEMP_FILE, '-enc', 'UTF-8'], shell=True)
        ls = []
        with open(TEMP_FILE, "r") as txtfile:
            output = txtfile.readlines()
            for row in output:
                splittedStr = row.split("-")
                if len(splittedStr) == 2:
                    ls.append(QuoteModel(
                        splittedStr[0].strip(), splittedStr[1].strip()))
        os.remove(TEMP_FILE)
        return ls
