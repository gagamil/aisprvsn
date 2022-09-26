from pathlib import Path
import tablib
from django.test import TestCase
from django.conf import settings

from importdata.resources import StockValueResource
from stocks.models import StockValue


class ImportTestCase(TestCase):
    def test_data_import_ok(self):
        ticker = 'GOOG'
        import_file = settings.BASE_DIR / 'data' / 'original' / f'{ticker}.csv'
        with import_file.open('r') as f:
            resource = StockValueResource(ticker)
            dataset = tablib.Dataset().load(f)
            resource.import_data(dataset, raise_errors=True)

        self.assertEqual(True, StockValue.objects.exists())
