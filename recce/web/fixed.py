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

class FixedViewMarkersView(LoginRequiredMixin, FormView):
    template_name = "recce/fixed_markers.html"
    form_class = FixedViewMarkerForm

    def dispatch(self, request, *args, **kwargs):
        self.fixed = get_object_or_404(InstallFixedView, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        m = form.save(commit=False)
        m.fixed_view = self.fixed
        m.save()
        messages.success(self.request, "Marker gespeichert.")
        return redirect("recce:fixed_markers", pk=self.fixed.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Template uses `fixed_view`.
        ctx["fixed_view"] = self.fixed
        ctx["install"] = self.fixed.install_option
        # Some DBs don't have created_at (older migrations) → order by id.
        ctx["markers"] = self.fixed.markers.all().order_by("-id")
        return ctx
class FixedViewMarkerDeleteView(LoginRequiredMixin, DeleteView):
    model = FixedViewMarker
    template_name = "recce/confirm_delete.html"

    def get_success_url(self):
        return reverse("recce:fixed_markers", kwargs={"pk": self.object.fixed_view_id})

# --------------------------
# Fixed views (4 slots) upsert
# --------------------------
class FixedViewUpsertView(LoginRequiredMixin, UpdateView):
    model = InstallFixedView
    form_class = FixedViewForm
    template_name = "recce/fixed_view_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.install = get_object_or_404(InstallOption, pk=kwargs["install_id"])
        self.view_type = kwargs["view_type"]
        obj, _ = InstallFixedView.objects.get_or_create(install_option=self.install, view_type=self.view_type)
        self.kwargs["pk"] = obj.pk
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Ansicht gespeichert.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("recce:install_detail", kwargs={"pk": self.object.install_option_id})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["install"] = self.install
        ctx["view_type"] = self.view_type
        return ctx

# --------------------------
# BatteryConfig + MaxSetup
# --------------------------
