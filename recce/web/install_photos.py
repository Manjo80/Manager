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

class InstallPhotoCreateView(LoginRequiredMixin, CreateView):
    model = InstallPhoto
    form_class = InstallPhotoForm
    template_name = "recce/install_photo_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.install = get_object_or_404(InstallOption, pk=kwargs["install_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.install_option = self.install
        obj.save()
        messages.success(self.request, "Foto hinzugefügt.")
        return redirect("recce:install_detail", pk=self.install.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["install"] = self.install
        return ctx
class InstallPhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = InstallPhoto
    template_name = "recce/confirm_delete.html"

    def get_success_url(self):
        return reverse("recce:install_detail", kwargs={"pk": self.object.install_option_id})


# --------------------------
# Markers (simple editor)
# --------------------------
class InstallPhotoMarkersView(LoginRequiredMixin, FormView):
    template_name = "recce/photo_markers.html"
    form_class = InstallPhotoMarkerForm

    def dispatch(self, request, *args, **kwargs):
        self.photo = get_object_or_404(InstallPhoto, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        m = form.save(commit=False)
        m.photo = self.photo
        m.save()
        messages.success(self.request, "Marker gespeichert.")
        return redirect("recce:install_photo_markers", pk=self.photo.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["photo"] = self.photo
        ctx["install"] = self.photo.install_option
        # No timestamps on marker model (and we don't need them).
        ctx["markers"] = self.photo.markers.all().order_by("-id")
        return ctx
class InstallPhotoMarkerDeleteView(LoginRequiredMixin, DeleteView):
    model = InstallPhotoMarker
    template_name = "recce/confirm_delete.html"

    def get_success_url(self):
        return reverse("recce:install_photo_markers", kwargs={"pk": self.object.photo_id})
