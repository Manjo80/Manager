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

from recce.web.utils import dedupe_case_insensitive


class VehicleFilterView(LoginRequiredMixin, ListView):
    model = RecceVehicle
    template_name = "recce/vehicle_filter.html"
    context_object_name = "vehicles"
    paginate_by = 50

    def get_queryset(self):
        qs = super().get_queryset()
        q = (self.request.GET.get("q") or "").strip()
        brand = (self.request.GET.get("brand") or "").strip()
        model = (self.request.GET.get("model") or "").strip()

        if q:
            qs = qs.filter(
                Q(brand__icontains=q)
                | Q(model__icontains=q)
                | Q(variant__icontains=q)
                | Q(description__icontains=q)
            )
        if brand:
            qs = qs.filter(brand__iexact=brand)
        if model:
            qs = qs.filter(model__iexact=model)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Filter dropdowns: brands + models (depend on chosen brand)
        ctx["brands"] = dedupe_case_insensitive(
            RecceVehicle.objects.values_list("brand", flat=True)
        )

        selected_brand = (self.request.GET.get("brand") or "").strip()
        if selected_brand:
            models_for_brand = RecceVehicle.objects.filter(brand__iexact=selected_brand).values_list("model", flat=True)
            ctx["models_for_brand"] = dedupe_case_insensitive(models_for_brand)
        else:
            ctx["models_for_brand"] = []

        ctx["selected_brand"] = selected_brand
        ctx["selected_model"] = (self.request.GET.get("model") or "").strip()
        ctx["q"] = (self.request.GET.get("q") or "").strip()
        return ctx


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = RecceVehicle
    form_class = VehicleForm
    template_name = "recce/vehicle_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.updated_by = self.request.user
        obj.save()

        # Optional multi-upload of photos
        files = self.request.FILES.getlist("photos")
        for f in files:
            VehiclePhoto.objects.create(vehicle=obj, image=f)

        messages.success(self.request, "Fahrzeug gespeichert.")
        return redirect("recce:vehicle_detail", pk=obj.pk)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = RecceVehicle
    form_class = VehicleForm
    template_name = "recce/vehicle_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()

        files = self.request.FILES.getlist("photos")
        for f in files:
            VehiclePhoto.objects.create(vehicle=obj, image=f)

        messages.success(self.request, "Fahrzeug gespeichert.")
        return redirect("recce:vehicle_detail", pk=obj.pk)


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = RecceVehicle
    template_name = "recce/confirm_delete.html"
    success_url = reverse_lazy("recce:vehicle_filter")


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = RecceVehicle
    template_name = "recce/vehicle_detail.html"
    context_object_name = "vehicle"
