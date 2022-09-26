from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import StockValueImportData
from .resources import StockValueResource


class StockValueImportDataAdmin(ImportExportModelAdmin):
    resource_class = StockValueResource
    search_fields = (
        "ticker",
    )

admin.site.register(StockValueImportData, StockValueImportDataAdmin)
