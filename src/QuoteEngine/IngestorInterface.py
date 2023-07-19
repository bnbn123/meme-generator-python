from abc import abstractmethod
from .QuoteModel import QuoteModel
from typing import List
import os


class IngestorInterface:
    valid_exts = ["csv", "pdf", "txt", "docx"]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        _, extension = os.path.splitext(path)
        return extension in cls.valid_exts

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
