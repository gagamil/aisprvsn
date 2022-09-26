from pathlib import Path
import tablib
from django.test import TestCase
from django.conf import settings

from .resources import StockValueResource


class ImportTestCase(TestCase):
    def test_data_import_ok(self):
        ticker = 'GOOG'
        import_file = settings.BASE_DIR / 'data' / 'original' / f'{ticker}.csv'
        with import_file.open('r') as f:
            resource = StockValueResource(ticker)
            dataset = tablib.Dataset().load(f)
            result = resource.import_data(dataset, dry_run=True, raise_errors=True)
            # print(result.has_errors())
