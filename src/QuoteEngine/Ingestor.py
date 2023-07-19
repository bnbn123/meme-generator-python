from .CsvIngestor import CsvIngestor
from .DocxIngestor import DocxIngestor
from .PdfIngestor import PdfIngestor
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor:
    ingestors = [CsvIngestor,
                 DocxIngestor,
                 PdfIngestor,
                 TextIngestor]

    def __init__(self, paths):
        self.paths = paths

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
