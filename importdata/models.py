from django.db import models

from common.models import BaseModelMixin


class StockValueImportData(BaseModelMixin):
    '''
    Use this as the import entry point - dirty data.
    '''
    ticker = models.CharField(max_length=5)
    date = models.DateField(blank=True)
    value_open = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_high = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_low = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_close = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_adjclose = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    volume = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.ticker}, {self.date}'