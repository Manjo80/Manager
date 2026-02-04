from django.db import models
from .common import ActiveModel

class SenderModel(ActiveModel):
    brand = models.CharField(max_length=120, db_index=True)
    name = models.CharField(max_length=120, db_index=True)
    photo = models.ImageField(upload_to="sender_models/", blank=True, null=True)

    has_audio = models.BooleanField(default=False)
    has_fixed_power = models.BooleanField(default=False)

    supported_batteries = models.ManyToManyField("settingsapp.BatteryType", blank=True, related_name="sender_models")
    profiles = models.ManyToManyField("settingsapp.Profile", blank=True, related_name="sender_models")

    class Meta:
        unique_together = [("brand", "name")]

    def __str__(self):
        return f"{self.brand} {self.name}"
