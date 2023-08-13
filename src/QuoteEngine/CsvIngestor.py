import sys
import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List

from QuoteEngine.helpers import read_csv_file

sys.path.append("../src")


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


class CsvIngestor(IngestorInterface):

    def parse(cls, path: str) -> List[QuoteModel]:
        return read_csv_file(path)
