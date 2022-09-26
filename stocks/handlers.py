import logging
from dataclasses import asdict
from django.dispatch import receiver

from common.signals import stockdata_import_done
from .models import StockValue

logger = logging.getLogger(__name__)


@receiver(stockdata_import_done)
def new_batch_imported(sender, **kwargs):
    '''
    This is run synronously. If things get hot move to async (if more logic is being added).
    The type of storage will depend on the data throughoutput and the use cases.
    '''
    stockdata = kwargs['stockdata']
    logger.debug(f'New StockValue will be created in handler. {stockdata.ticker=} {stockdata.date=}')
    try:
        StockValue.objects.create(**asdict(stockdata))
    except Exception as exc:
        logger.error(f'During StockValue creation an exception occured: {exc}')
