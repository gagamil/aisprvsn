from import_export import resources

from .models import StockValueImportData


class StockValueResource(resources.ModelResource):
    class Meta:
        model = StockValueImportData
        fields = ('id', 'date', 'value_open', 'value_high', 'value_low', 'value_close', 'value_adjclose', 'volume')

    def before_import_row(self, row, row_number=None, **kwargs):
        print(row, row_number, kwargs)