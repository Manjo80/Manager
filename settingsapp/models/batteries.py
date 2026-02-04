from django.db import models
from .common import ActiveModel

class BatteryType(ActiveModel):
    name = models.CharField(max_length=120, unique=True, db_index=True)
    brand = models.CharField(max_length=120, blank=True, default="")
    capacity_mah = models.PositiveIntegerField()
    voltage_v = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to="batterytypes/", blank=True, null=True)

    def __str__(self):
        return self.name
