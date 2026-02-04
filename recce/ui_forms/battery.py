from __future__ import annotations

from django import forms

from recce.models import BatteryConfig


class BatteryConfigForm(forms.ModelForm):
    class Meta:
        model = BatteryConfig
        fields = [
            "name",
            "battery_type",
            "cells_count",
            "arrangement",
            "capacity_mah",
            "voltage_v",
            "photo",
        ]
