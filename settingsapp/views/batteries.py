from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import BatteryType

class List(SettingsListView):
    model = BatteryType
    extra_context = {"title": "Akkus"}

class Create(SettingsCreateView):
    model = BatteryType
    fields = ["name", "brand", "capacity_mah", "voltage_v", "photo", "active"]
    success_url = reverse_lazy("settingsapp:batterytype_list")
    extra_context = {"title": "Akkus – Neu"}

class Update(SettingsUpdateView):
    model = BatteryType
    fields = ["name", "brand", "capacity_mah", "voltage_v", "photo", "active"]
    success_url = reverse_lazy("settingsapp:batterytype_list")
    extra_context = {"title": "Akkus – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = BatteryType
    success_url = reverse_lazy("settingsapp:batterytype_list")
    extra_context = {"title": "Akkus – Löschen"}
