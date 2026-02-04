from __future__ import annotations

from django import forms

from recce.models import RecceVehicle, VehiclePhoto


class VehicleForm(forms.ModelForm):
    class Meta:
        model = RecceVehicle
        fields = ["brand", "model", "variant", "year_from", "year_to", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class VehiclePhotoForm(forms.ModelForm):
    # allow multi-upload in create view (views can read request.FILES.getlist)
    image = forms.ImageField(required=True)

    class Meta:
        model = VehiclePhoto
        fields = ["perspective", "image", "caption", "order"]
        widgets = {
            "caption": forms.Textarea(attrs={"rows": 2}),
        }
