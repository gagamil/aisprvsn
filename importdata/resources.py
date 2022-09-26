from import_export import resources

from .models import StockValueImportData


class StockValueResource(resources.ModelResource):
    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
    class Meta:
        model = StockValueImportData
        fields = ('id', 'date', 'value_open', 'value_high', 'value_low', 'value_close', 'value_adjclose', 'volume')

    def before_import_row(self, row, row_number=None, **kwargs):
        row['ticker'] = self.ticker
        print(row, row_number, kwargs)