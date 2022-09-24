from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import StockValueImportData


class StockValueResource(resources.ModelResource):
    class Meta:
        model = StockValueImportData
        fields = ('id', 'ticker', 'date', 'value_open', 'value_high', 'value_low', 'value_close', 'value_adjclose', 'volume')


class StockValueImportDataAdmin(ImportExportModelAdmin):
    resource_class = StockValueResource
    search_fields = (
        "ticker",
    )

admin.site.register(StockValueImportData, StockValueImportDataAdmin)
