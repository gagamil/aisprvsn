from rest_framework import serializers

from .models import StockValue


class StockValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockValue
        fields = ['id', 'ticker', 'date', 'value_open', 'value_high', 'value_low', 'value_close', 'value_adjclose', 'volume']
