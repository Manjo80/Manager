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

class BatteryConfigCreateView(LoginRequiredMixin, CreateView):
    model = BatteryConfig
    form_class = BatteryConfigForm
    template_name = "recce/batteryconfig_form.html"

    def form_valid(self, form):
        messages.success(self.request, "BatteryConfig angelegt.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("recce:vehicle_filter")
