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
    print("Ingestor path", ingestors)

    def parse(path) -> List[QuoteModel]:
        """Docstring for parse function."""
        print("Ingestor path", path)
        splittedPath = path.split(".")
        extension = splittedPath[-1]
        print("Ingestor extension", extension)

        try:
            isCanIngest = IngestorInterface.can_ingest(extension)
            if not isCanIngest:
                raise Exception(
                    "Should import file with extension belong to [csv, pdf, docx, txt]"
                )

            if extension == "csv":
                Ingestor.ingestors.extend(CsvIngestor().parse(path))
            elif extension == "pdf":
                Ingestor.ingestors.extend(PdfIngestor().parse(path))
            elif extension == "docx":
                Ingestor.ingestors.extend(DocxIngestor().parse(path))
            elif extension == "txt":
                Ingestor.ingestors.extend(TextIngestor().parse(path))
            return Ingestor.ingestors
        except Exception as err:
            print(*err.args)
