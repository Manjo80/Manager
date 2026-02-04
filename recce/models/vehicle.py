from django.db import models
from django.contrib.auth import get_user_model
from settingsapp.models.recce_perspectives import ReccePerspective

User = get_user_model()

class RecceVehicle(models.Model):
    brand = models.CharField(max_length=80, db_index=True)
    model = models.CharField(max_length=80, db_index=True)
    variant = models.CharField(max_length=120, blank=True, default="", db_index=True)
    year_from = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    year_to = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="recce_vehicle_created")
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="recce_vehicle_updated")

    class Meta:
        ordering = ["brand", "model", "variant", "year_from"]

    def __str__(self):
        years = ""
        if self.year_from or self.year_to:
            years = f" ({self.year_from or ''}-{self.year_to or ''})"
        v = f" {self.variant}" if self.variant else ""
        return f"{self.brand} {self.model}{v}{years}".strip()

class VehiclePhoto(models.Model):
    vehicle = models.ForeignKey(RecceVehicle, on_delete=models.CASCADE, related_name="photos")
    perspective = models.ForeignKey(ReccePerspective, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="recce/vehicle/")
    caption = models.TextField(blank=True, default="")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Photo {self.id} for {self.vehicle}"
