from django.db import models
from settingsapp.models import SenderModel, Group

class Sender(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "available", "Verfügbar"
        IN_USE = "in_use", "Im Einsatz"
        DEFECT = "defect", "Defekt"
        LOST = "lost", "Verloren"

    # Eure ID
    name = models.CharField(max_length=80, unique=True, db_index=True)

    phone_number = models.CharField(max_length=40, blank=True, default="")
    model = models.ForeignKey(SenderModel, on_delete=models.PROTECT, related_name="senders")

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True, blank=True, related_name="senders")

    note = models.TextField(blank=True, default="")

    def save(self, *args, **kwargs):
        # Gruppe nur bei verfügbar
        if self.status != self.Status.AVAILABLE:
            self.group = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
