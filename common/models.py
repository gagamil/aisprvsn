from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel, UUIDModel


class BaseModelMixin(TimeStampedModel, SoftDeletableModel):
    class Meta:
        abstract = True
