from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from recce.forms import (
    BatteryConfigForm,
    FixedViewForm,
    FixedViewMarkerForm,
    InstallOptionForm,
    InstallPhotoForm,
    InstallPhotoMarkerForm,
    MaxSetupForm,
    VehicleForm,
    VehiclePhotoForm,
)
from recce.models import (
    BatteryConfig,
    FixedViewMarker,
    InstallFixedView,
    InstallOption,
    InstallOptionMaxSetup,
    InstallPhoto,
    InstallPhotoMarker,
    RecceVehicle,
    VehiclePhoto,
)

class VehiclePhotoCreateView(LoginRequiredMixin, CreateView):
    model = VehiclePhoto
    form_class = VehiclePhotoForm
    template_name = "recce/vehicle_photo_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.vehicle = get_object_or_404(RecceVehicle, pk=kwargs["vehicle_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.vehicle = self.vehicle
        obj.save()
        messages.success(self.request, "Foto gespeichert.")
        return redirect("recce:vehicle_detail", pk=self.vehicle.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["vehicle"] = self.vehicle
        return ctx


class VehiclePhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = VehiclePhoto
    template_name = "recce/confirm_delete.html"

    def get_success_url(self):
        return reverse("recce:vehicle_detail", kwargs={"pk": self.object.vehicle_id})
