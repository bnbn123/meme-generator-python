from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from QuoteEngine.helpers import read_docx_file


class DocxIngestor(IngestorInterface):

    def parse(cls, path: str) -> List[QuoteModel]:
        return read_docx_file(path)
