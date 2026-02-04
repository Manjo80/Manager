from __future__ import annotations

from django import forms

from recce.models import InstallOptionMaxSetup


class MaxSetupForm(forms.ModelForm):
    class Meta:
        model = InstallOptionMaxSetup
        fields = ["sender_model", "power_mode", "max_battery_config", "notes"]
        widgets = {"notes": forms.Textarea(attrs={"rows": 3})}
