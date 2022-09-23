import factory
from .models import StockValue


class StockValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockValue

    # ticker = factory.Faker('name')
    # date = factory.Faker('date', end_datetime=datetime.date.today())
    # value_open = factory.Faker('date', end_datetime=datetime.date.today())
    # value_high = factory.Faker('date', end_datetime=datetime.date.today())
    # value_low = factory.Faker('date', end_datetime=datetime.date.today())
    # value_close = factory.Faker('date', end_datetime=datetime.date.today())
    # value_adjclose = factory.Faker('date', end_datetime=datetime.date.today())
    # volume = factory.Faker('date', end_datetime=datetime.date.today())
