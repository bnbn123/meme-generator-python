from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from QuoteEngine.helpers import read_text_file


class TextIngestor(IngestorInterface):

    def parse(cls, path: str) -> List[QuoteModel]:
        return read_text_file(path)
