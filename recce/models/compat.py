from django.db import models
from settingsapp.models.sender_models import SenderModel
from settingsapp.models.batteries import BatteryType

class BatteryConfig(models.Model):
    """Reusable battery configuration definition (the 'combo')."""
    name = models.CharField(max_length=120, unique=True)
    battery_type = models.ForeignKey(BatteryType, null=True, blank=True, on_delete=models.SET_NULL)
    cells_count = models.PositiveIntegerField(default=1)
    arrangement = models.CharField(
        max_length=16,
        choices=[("series","Serie"),("parallel","Parallel"),("custom","Custom")],
        default="custom",
    )
    capacity_mah = models.PositiveIntegerField(null=True, blank=True)
    voltage_v = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    photo = models.ImageField(upload_to="recce/batteryconfigs/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class InstallOptionMaxSetup(models.Model):
    """For each InstallOption + SenderModel exactly ONE max setup."""
    class PowerMode(models.TextChoices):
        BATTERY_ONLY = "battery_only", "Nur Batterie"
        HARDWIRE_ONLY = "hardwire_only", "Nur Feststrom"
        EITHER = "either", "Batterie oder Feststrom"

    # Backwards-compatible alias used by older code/templates.
    POWER_CHOICES = PowerMode.choices

    install_option = models.ForeignKey("recce.InstallOption", on_delete=models.CASCADE, related_name="max_setups")
    sender_model = models.ForeignKey(SenderModel, on_delete=models.CASCADE)
    power_mode = models.CharField(max_length=20, choices=PowerMode.choices, default=PowerMode.EITHER)
    max_battery_config = models.ForeignKey(BatteryConfig, null=True, blank=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, default="")

    class Meta:
        unique_together = [("install_option", "sender_model")]
        ordering = ["install_option", "sender_model"]

    def __str__(self):
        return f"{self.install_option} - {self.sender_model}"
