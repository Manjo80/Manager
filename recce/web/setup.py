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

class MaxSetupUpsertView(LoginRequiredMixin, CreateView):
    model = InstallOptionMaxSetup
    form_class = MaxSetupForm
    template_name = "recce/setup_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.install = get_object_or_404(InstallOption, pk=kwargs["install_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.install_option = self.install
        try:
            obj.save()
        except Exception:
            form.add_error("sender_model", "Für diesen Sender existiert bereits eine Max-Kombo.")
            return self.form_invalid(form)
        messages.success(self.request, "Max-Kombo gespeichert.")
        return redirect("recce:install_detail", pk=self.install.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["install"] = self.install
        return ctx
class MaxSetupDeleteView(LoginRequiredMixin, DeleteView):
    model = InstallOptionMaxSetup
    template_name = "recce/confirm_delete.html"

    def get_success_url(self):
        return reverse("recce:install_detail", kwargs={"pk": self.object.install_option_id})
