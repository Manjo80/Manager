from __future__ import annotations

from django import forms

from recce.models import InstallOption, InstallPhoto, InstallFixedView


class InstallOptionForm(forms.ModelForm):
    class Meta:
        model = InstallOption
        fields = [
            "title",
            "description",
            "tools",
            "risk_level",
            "effort_minutes",
            "installed_by",
            "installed_on",
            "fixed_power",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "installed_on": forms.DateInput(attrs={"type": "date"}),
        }


class InstallPhotoForm(forms.ModelForm):
    class Meta:
        model = InstallPhoto
        fields = ["image", "caption", "order"]
        widgets = {
            "caption": forms.Textarea(attrs={"rows": 2}),
        }


class FixedViewForm(forms.ModelForm):
    class Meta:
        model = InstallFixedView
        fields = ["image", "caption"]
        widgets = {
            "caption": forms.Textarea(attrs={"rows": 2}),
        }
