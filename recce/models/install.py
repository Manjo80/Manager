from django.db import models
from django.contrib.auth import get_user_model

from settingsapp.models.people import Person
from settingsapp.models.tools import Tool
from settingsapp.models.risk_levels import RiskLevel
from .vehicle import RecceVehicle

User = get_user_model()

class InstallOption(models.Model):
    vehicle = models.ForeignKey(RecceVehicle, on_delete=models.CASCADE, related_name="install_options")
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, default="")
    tools = models.ManyToManyField(Tool, blank=True)
    risk_level = models.ForeignKey(RiskLevel, null=True, blank=True, on_delete=models.SET_NULL)
    effort_minutes = models.PositiveIntegerField(null=True, blank=True)

    # Who installed it, and when (date only).
    installed_by = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recce_installoptions",
        verbose_name="Wer",
    )
    installed_on = models.DateField(null=True, blank=True, verbose_name="Wann")

    # Optional: hardwired / fixed power.
    fixed_power = models.BooleanField(default=False, verbose_name="Feststrom")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="recce_install_created")
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="recce_install_updated")

    class Meta:
        ordering = ["vehicle", "title"]

    def __str__(self):
        return f"{self.vehicle}: {self.title}"

class InstallPhoto(models.Model):
    install_option = models.ForeignKey(InstallOption, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="recce/install/")
    caption = models.TextField(blank=True, default="")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

class InstallFixedView(models.Model):
    class ViewType(models.TextChoices):
        FRONT = "front", "Front"
        REAR = "rear", "Heck"
        TOP = "top", "Top"
        SIDE = "side", "Seite"

    install_option = models.ForeignKey(InstallOption, on_delete=models.CASCADE, related_name="fixed_views")
    view_type = models.CharField(max_length=10, choices=ViewType.choices)
    image = models.ImageField(upload_to="recce/fixed/", blank=True, null=True)
    caption = models.TextField(blank=True, default="")

    class Meta:
        unique_together = [("install_option", "view_type")]

    def __str__(self):
        return f"{self.install_option} [{self.view_type}]"
