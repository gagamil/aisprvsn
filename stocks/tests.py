from rest_framework.test import APITestCase
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse

from .models import StockValue
from .factory import StockValueFactory


class SimpleStockCRUDAPITestCase(APITestCase):
    def setUp(self):
        today = timezone.now() # caution - will work if the rest is created the same day (12:59:59 might fail)
        for i in range(3):
            StockValueFactory(date=today-timedelta(days=2))
        for i in range(3):
            StockValueFactory(date=today-timedelta(days=4))
        for i in range(3):
            StockValueFactory(date=today-timedelta(days=8))

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