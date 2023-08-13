"""Docstring for IngestorInterface's module."""
from abc import abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface:
    """Docstring for IngestorInterface's abstract class."""

    @classmethod
    def can_ingest(cls, suffix: str) -> bool:
        """Docstring for can_ingest function."""
        return (
            True
            if suffix == "csv" or suffix == "pdf" or suffix == "txt" or suffix == "docx"
            else False
        )

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Docstring for parse function."""
        pass
