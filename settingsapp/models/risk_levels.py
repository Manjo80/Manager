from django.db import models
from .common import ActiveModel

class RiskLevel(ActiveModel):
    value = models.IntegerField(unique=True)
    label = models.CharField(max_length=80)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "value"]

    def __str__(self):
        return f"{self.value} - {self.label}"
