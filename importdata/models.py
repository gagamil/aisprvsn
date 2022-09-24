from django.db import models

from common.models import BaseModelMixin
from common.signals import sig_send__stockdata_import_done
from common.data import StockData
from common.const import DECIMAL_PLACES_MULTIPLIER

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stock_data_object = StockData(
                                        id=self.pk,
                                        ticker=self.ticker,
                                        value_open=self.value_open * DECIMAL_PLACES_MULTIPLIER,
                                        value_high=self.value_high * DECIMAL_PLACES_MULTIPLIER,
                                        value_low=self.value_low * DECIMAL_PLACES_MULTIPLIER,
                                        value_close=self.value_close * DECIMAL_PLACES_MULTIPLIER,
                                        value_adjclose=self.value_adjclose * DECIMAL_PLACES_MULTIPLIER,
                                        volume=self.volume
                                    )
        sig_send__stockdata_import_done(sender=self, sender_pk=self.pk, stockdata=stock_data_object)
        return