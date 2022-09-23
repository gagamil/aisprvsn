from django.urls import path, include

from .views import StockValueListAPIView, StockValueDetailAPIView


urlpatterns = [
    path('stock/', StockValueListAPIView.as_view(), name='api-get-list-stocks'),
    path('stock/<int:pk>/', StockValueDetailAPIView.as_view(), name='api-get-detail-stock'),
]
