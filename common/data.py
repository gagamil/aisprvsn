from dataclasses import dataclass
from datetime import date
from typing import List
# from dataclasses_json import dataclass_json


@dataclass
class StockData:
    id: int
    ticker: str
    date: date
    value_open: float
    value_high: float
    value_low: float
    value_close: float
    value_adjclose: float
    volume: int