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

from recce.web.utils import require_sender_model


def _map_power_mode(value: str) -> str:
    """Accept legacy values ('battery','fixed','either') and newer enum values.

    Returns a value that is safe to store into InstallOptionMaxSetup.power_mode.
    """
    v = (value or "").strip()
    if not v:
        return v

    legacy_map = {
        "battery": getattr(InstallOptionMaxSetup, "POWER_BATTERY", None),
        "fixed": getattr(InstallOptionMaxSetup, "POWER_FIXED", None),
    }
    if v in legacy_map and legacy_map[v]:
        return legacy_map[v]

    # Accept enum values as-is
    return v


def _handle_install_extras(request, install: InstallOption, form):
    SenderModel = require_sender_model(request)
    if SenderModel is None:
        return

    fixed_power_all = request.POST.get("fixed_power_all") in ("1", "on", "true", "True")

    selected = []
    for sm in SenderModel.objects.all().order_by("name"):
        if request.POST.get(f"sm_{sm.id}") != "on":
            continue

        bc_id = request.POST.get(f"bc_{sm.id}") or ""
        pm_raw = request.POST.get(f"pm_{sm.id}") or ""
        pm = _map_power_mode(pm_raw) or getattr(InstallOptionMaxSetup, "POWER_BATTERY", InstallOptionMaxSetup.PowerMode.EITHER)

        if fixed_power_all:
            pm = getattr(InstallOptionMaxSetup, "POWER_FIXED", InstallOptionMaxSetup.PowerMode.HARDWIRE_ONLY)
            bc_id = ""

        battery_config = None
        if bc_id.isdigit():
            candidate = BatteryConfig.objects.filter(id=int(bc_id)).first()
            if candidate and hasattr(sm, "supported_battery_types"):
                if sm.supported_battery_types.filter(id=candidate.battery_type_id).exists():
                    battery_config = candidate

        selected.append((sm, pm, battery_config))

    InstallOptionMaxSetup.objects.filter(install_option=install).delete()
    for sm, pm, bc in selected:
        InstallOptionMaxSetup.objects.create(
            install_option=install,
            sender_model=sm,
            power_mode=pm,
            max_battery_config=bc,
            notes="",
        )


def _install_setup_context(request, install: InstallOption | None):
    SenderModel = require_sender_model(request)
    sender_models = list(SenderModel.objects.all().order_by("name")) if SenderModel else []

    battery_configs = list(BatteryConfig.objects.all().order_by("-capacity_mah", "name"))
    default_battery_id = battery_configs[0].id if battery_configs else None

    existing = {}
    if install and install.pk:
        for ms in install.max_setups.select_related("sender_model", "max_battery_config").all():
            existing[ms.sender_model_id] = ms

    setup_rows = []
    for sm in sender_models:
        allowed_bt_ids = list(getattr(sm, "supported_battery_types").values_list("id", flat=True)) if hasattr(sm, "supported_battery_types") else []
        default_bc_id = None
        if allowed_bt_ids:
            for bc in battery_configs:
                if bc.battery_type_id in allowed_bt_ids:
                    default_bc_id = bc.id
                    break
        setup_rows.append(
            {
                "sender_model": sm,
                "setup": existing.get(sm.id),
                "allowed_battery_type_ids": allowed_bt_ids,
                "default_battery_config_id": default_bc_id or default_battery_id,
            }
        )

    power_modes = getattr(InstallOptionMaxSetup, "POWER_CHOICES", None) or getattr(InstallOptionMaxSetup.PowerMode, "choices", [])

    return {
        "battery_configs": battery_configs,
        "default_battery_config_id": default_battery_id,
        "setup_rows": setup_rows,
        "power_modes": power_modes,
    }


class InstallOptionCreateView(LoginRequiredMixin, CreateView):
    model = InstallOption
    form_class = InstallOptionForm
    template_name = "recce/install_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.vehicle = get_object_or_404(RecceVehicle, pk=kwargs["vehicle_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.vehicle = self.vehicle
        obj.created_by = self.request.user
        obj.updated_by = self.request.user
        obj.save()
        form.save_m2m()

        _handle_install_extras(self.request, obj, form)

        messages.success(self.request, "Einbau-Option gespeichert.")
        return redirect("recce:install_detail", pk=obj.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["vehicle"] = self.vehicle
        ctx["install"] = None
        ctx.update(_install_setup_context(self.request, install=None))
        return ctx


class InstallOptionUpdateView(LoginRequiredMixin, UpdateView):
    model = InstallOption
    form_class = InstallOptionForm
    template_name = "recce/install_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()
        form.save_m2m()

        _handle_install_extras(self.request, obj, form)

        messages.success(self.request, "Einbau-Option gespeichert.")
        return redirect("recce:install_detail", pk=obj.pk)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["vehicle"] = self.object.vehicle
        ctx["install"] = self.object
        ctx.update(_install_setup_context(self.request, install=self.object))
        return ctx
class InstallOptionDeleteView(LoginRequiredMixin, DeleteView):
    model = InstallOption
    template_name = "recce/confirm_delete.html"

    def get_success_url(self):
        messages.warning(self.request, "Einbaumöglichkeit gelöscht.")
        return reverse("recce:vehicle_detail", kwargs={"pk": self.object.vehicle_id})
class InstallOptionDetailView(LoginRequiredMixin, DetailView):
    model = InstallOption
    template_name = "recce/install_detail.html"


def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    install = self.object

    # Build marker JSON for photos so the UI can render overlays + numbering.
    # Numbering is continuous per InstallOption across all photos (ordered by photo.order/id and marker.order/id).
    photo_markers = {}
    counter = 0
    photos = install.photos.all().order_by("order", "id")
    for p in photos:
        markers_qs = p.markers.all().order_by("order", "id")
        items = []
        for m in markers_qs:
            counter += 1
            items.append({
                "id": m.id,
                "n": counter,
                "type": m.marker_type,
                "x": float(m.x),
                "y": float(m.y),
                "w": float(m.w) if m.w is not None else None,
                "h": float(m.h) if m.h is not None else None,
                "r": float(m.r) if m.r is not None else None,
                "x2": float(m.x2) if m.x2 is not None else None,
                "y2": float(m.y2) if m.y2 is not None else None,
                "note": (m.note or "").strip(),
            })
        photo_markers[str(p.id)] = items

    ctx["photo_markers_json"] = photo_markers
    return ctx
    context_object_name = "install"

# --------------------------
# Install photos
# --------------------------
