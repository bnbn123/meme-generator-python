"""Docstring for Ingestor's module."""
from .CsvIngestor import CsvIngestor
from .DocxIngestor import DocxIngestor
from .PdfIngestor import PdfIngestor
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List


class Ingestor:
    """Docstring for Ingestor's class."""

    ingestors = []

    def parse(path) -> List[QuoteModel]:
        """Docstring for parse function."""
        splittedPath = path.split(".")
        extension = splittedPath[-1]

        try:
            isCanIngest = IngestorInterface.can_ingest(extension)
            if not isCanIngest:
                raise Exception(
                    "Should import file with extension belong to [csv, pdf, docx, txt]"
                )
            # have to type safe this to possibly throw exception
            parsedData: List[QuoteModel] = []
            if extension == "csv":
                parsedData = CsvIngestor().parse(path)
            elif extension == "pdf":
                parsedData = PdfIngestor().parse(path)
            elif extension == "docx":
                parsedData = DocxIngestor().parse(path)
            elif extension == "txt":
                parsedData = TextIngestor().parse(path)

            if len(parsedData) == 0:
                raise Exception(
                    "Import success. No data in found file or wrong file content.")
            # reuse the same list in app.py
            Ingestor.ingestors.extend(parsedData)
            return Ingestor.ingestors
        # could improve this part by using custom exception
        except Exception as err:
            print(*err.args)
