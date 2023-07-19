from helpers import read_csv_file
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import os
import sys

sys.path.append("../src")


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


class CsvIngestor(IngestorInterface):

    def parse(cls, path: str) -> List[QuoteModel]:
        return read_csv_file(path)
