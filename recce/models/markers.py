from django.db import models


class MarkerBase(models.Model):
    class MarkerType(models.TextChoices):
        RECT = "rect", "Rechteck"
        CIRCLE = "circle", "Kreis"
        CROSS = "cross", "Kreuz"
        ARROW = "arrow", "Pfeil"

    marker_type = models.CharField(max_length=10, choices=MarkerType.choices, default=MarkerType.RECT)

    # Normalized coordinates (0..1) relative to the underlying image
    x = models.FloatField(help_text="0..1 (start/center)")
    y = models.FloatField(help_text="0..1 (start/center)")

    # Rect
    w = models.FloatField(null=True, blank=True, help_text="0..1 (rect width)")
    h = models.FloatField(null=True, blank=True, help_text="0..1 (rect height)")

    # Circle
    r = models.FloatField(null=True, blank=True, help_text="0..1 (circle radius)")

    # Arrow end
    x2 = models.FloatField(null=True, blank=True, help_text="0..1 (arrow end x)")
    y2 = models.FloatField(null=True, blank=True, help_text="0..1 (arrow end y)")

    label = models.CharField(max_length=120, blank=True, default="")
    note = models.TextField(blank=True, default="")
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class InstallPhotoMarker(MarkerBase):
    photo = models.ForeignKey("recce.InstallPhoto", on_delete=models.CASCADE, related_name="markers")


class FixedViewMarker(MarkerBase):
    fixed_view = models.ForeignKey("recce.InstallFixedView", on_delete=models.CASCADE, related_name="markers")
