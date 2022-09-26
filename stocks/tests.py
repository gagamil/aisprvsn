from datetime import timedelta
from random import randrange
from typing import List
from dataclasses import dataclass
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase

from common.const import DECIMAL_PLACES_MULTIPLIER
from .models import StockValue, STCK_SYMBOL__GOOG, StockSymbol
from .factory import StockValueFactory


# HELPERS
@dataclass
class FloorCeleingTestValue:
    val_floor: int
    val_celeing: int
    val_open: int
    val_close: int
    delta: int
    base: int


def get_floor_celeing_delta(*, base_value: int =0) -> FloorCeleingTestValue:
    '''
    Naive way to imitate daily historical data
    Goal is to populate these:
        value_open, value_high, value_low, value_close, value_adjclose
    Representation of the stock value:
    120.123456 => 120123456, 1.123456 => 1123456
    '''
    LOWEST_POSSIBLE_VALUE = 1 * DECIMAL_PLACES_MULTIPLIER # 1 USD
    HIGHEST_POSSIBLE_VALUE = 64000 * DECIMAL_PLACES_MULTIPLIER # 64000 USD
    if base_value == 0:
        base_value = randrange(LOWEST_POSSIBLE_VALUE, HIGHEST_POSSIBLE_VALUE)
    else:
        base_value = randrange(base_value - int(base_value / 20), base_value + int(base_value / 20))

    delta = int(base_value / 20) # approx 5% left and right 
    val_floor=base_value-delta
    val_celeing=base_value+delta

    result = FloorCeleingTestValue(
                                    val_floor=val_floor,
                                    val_celeing=val_celeing,
                                    val_open=randrange(val_floor, val_celeing),
                                    val_close=randrange(val_floor, val_celeing),
                                    delta=delta,
                                    base=base_value
                                    )
    return result

# TEST CASES
class SimpleStockCRUDAPITestCase(APITestCase):
    def setUp(self):
        today = timezone.now() # caution - will work if the rest is created the same day (12:59:59 might fail)

        values = get_floor_celeing_delta()
        base_value = values.base
        ss, _ = StockSymbol.objects.get_or_create(symbol=STCK_SYMBOL__GOOG)
        for i in range(9):
            StockValueFactory(
                                ticker=STCK_SYMBOL__GOOG,
                                symbol=ss,
                                date=today-timedelta(days=i),
                                value_open = values.val_open,
                                value_high = values.val_celeing,
                                value_low = values.val_floor,
                                value_close = values.val_close,
                                value_adjclose = values.val_close,
                                volume = randrange(10000, 100000)
                                )
            values = get_floor_celeing_delta(base_value=base_value)
            base_value = values.base

    def test_get_list_200(self):
        self.assertEqual(9, StockValue.objects.count())

        url = reverse('api-1.0.0:api-get-list-stocks')
        response = self.client.get(url, data={}, format='json')
        print(response.content)
        self.assertEqual(200, response.status_code)

    def test_get_detai_200(self):
        sv = StockValue.objects.first()
        url = reverse('api-1.0.0:api-get-detail-stock', kwargs={'record_id':sv.pk})
        response = self.client.get(url, data={}, format='json')
        print(response.content)
        self.assertEqual(200, response.status_code)


class FloorCeleingTestCase(TestCase):
    def test_basic_values_match(self):
        values = get_floor_celeing_delta()

        self.assertEqual(True, values.val_floor < values.val_celeing)
