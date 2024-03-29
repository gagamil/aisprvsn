from datetime import date
from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, ModelSchema
from ninja.pagination import paginate
from .models import StockValue

api = NinjaAPI()

class StockValueSchema(ModelSchema):
    class Config:
        model = StockValue
        model_fields = ['id', 'ticker', 'date', 'value_open', 'value_high', 'value_low', 'value_close', 'value_adjclose', 'volume']

@api.get("/stocks", response=List[StockValueSchema], url_name='api-get-list-stocks')
@paginate
def list_stocks(request, date_from: date = '', date_till:date = '', ticker:str = ''):
    qs = StockValue.objects.all()
    if date_from and date_till:
        qs = qs.filter(date__range=[date_from, date_till])
    if ticker:
        qs = qs.filter(ticker=ticker)
    return qs


@api.get("/stocks/{record_id}", response=StockValueSchema, url_name='api-get-detail-stock')
def read_item(request, record_id):
    return get_object_or_404(StockValue, id=record_id)
