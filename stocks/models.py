from django.db import models
from common.models import BaseModelMixin


STCK_SYMBOL__GOOG = 'GOOG'
STCK_SYMBOL__PLTR = 'PLTR'
STCK_SYMBOL__TWTR = 'TWTR'
STCK_SYMBOL__SAP = 'SAP'
STCK_SYMBOL__CHOICES = (
                        (STCK_SYMBOL__GOOG, 'Alphabet Inc.'),
                        (STCK_SYMBOL__PLTR, 'Palantir Technologies Inc.'),
                        (STCK_SYMBOL__TWTR, 'Twitter, Inc.'),
                        (STCK_SYMBOL__SAP, 'SAP SE')
                       )



class StockValue(BaseModelMixin):
    '''
    - ticker <-> symbol
    - all the value_ prefixed values are presented in the least possible denominatios (cents)
    '''
    ticker = models.CharField(choices=STCK_SYMBOL__CHOICES, max_length=5)
    date = models.DateField()
    value_open = models.PositiveIntegerField()
    value_high = models.PositiveIntegerField()
    value_low = models.PositiveIntegerField()
    value_close = models.PositiveIntegerField()
    value_adjclose = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.ticker}, {self.date}'

    class Meta:
        unique_together = ('ticker', 'date')
