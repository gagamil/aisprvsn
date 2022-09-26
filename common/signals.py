import logging
import django.dispatch

from common.data import StockData

logger = logging.getLogger(__name__)

stockdata_import_done = django.dispatch.Signal()
def sig_send__stockdata_import_done(*, sender, sender_pk: int, stockdata: StockData) -> None:
    logger.info(f'SIG "sig_send__stockdata_import_done" will be sent with imported stock data. Import ID: {sender_pk=}')
    stockdata_import_done.send(sender=sender, sender_pk=sender_pk, stockdata=stockdata)
