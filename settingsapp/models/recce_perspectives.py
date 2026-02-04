from django.db import models
from .common import ActiveModel

class ReccePerspective(ActiveModel):
    key = models.CharField(max_length=40, unique=True, db_index=True)
    label = models.CharField(max_length=80)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "label"]

    def __str__(self):
        return self.label
