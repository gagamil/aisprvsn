# from rest_framework import generics
# from django_filters import rest_framework as filters

# from .models import StockValue
# from .serializers import StockValueSerializer


# class StockValueFilter(filters.FilterSet):
#     min_value_close = filters.NumberFilter(field_name="value_close", lookup_expr='gte')
#     max_value_close = filters.NumberFilter(field_name="value_close", lookup_expr='lte')
#     min_date = filters.DateFilter(field_name="date", lookup_expr='gte')
#     max_date = filters.DateFilter(field_name="date", lookup_expr='lte')

#     class Meta:
#         model = StockValue
#         fields = ['ticker']


# class StockValueListAPIView(generics.ListAPIView):
#     queryset = StockValue.objects.all()
#     serializer_class = StockValueSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = StockValueFilter


# class StockValueDetailAPIView(generics.RetrieveAPIView):
#     queryset = StockValue.objects.all()
#     serializer_class = StockValueSerializer
