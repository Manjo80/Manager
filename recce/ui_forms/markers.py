from __future__ import annotations

from django import forms

from recce.models import InstallPhotoMarker, FixedViewMarker


class InstallPhotoMarkerForm(forms.ModelForm):
    class Meta:
        model = InstallPhotoMarker
        fields = [
            "marker_type",
            "x",
            "y",
            "w",
            "h",
            "r",
            "label",
            "note",
            "order",
        ]
        widgets = {
            "note": forms.Textarea(attrs={"rows": 3}),
        }


class FixedViewMarkerForm(forms.ModelForm):
    class Meta:
        model = FixedViewMarker
        fields = [
            "marker_type",
            "x",
            "y",
            "w",
            "h",
            "r",
            "label",
            "note",
            "order",
        ]
        widgets = {
            "note": forms.Textarea(attrs={"rows": 3}),
        }
