from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from helpers import read_pdf_file


class PdfIngestor(IngestorInterface):

    def parse(cls, path: str) -> List[QuoteModel]:
        return read_pdf_file(path)
