from django.db import models


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


class StockValue(models.Model):
    ticker = models.CharField(choices=STCK_SYMBOL__CHOICES, max_length=5)
    date = models.DateField()
    value_open = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_high = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_low = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_close = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    value_adjclose = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    volume = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.ticker}, {self.date}'
