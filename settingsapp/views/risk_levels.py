from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import RiskLevel

class List(SettingsListView):
    model = RiskLevel
    extra_context = {"title": "Risk-Level"}

class Create(SettingsCreateView):
    model = RiskLevel
    fields = ["value", "label", "order", "active"]
    success_url = reverse_lazy("settingsapp:risklevel_list")
    extra_context = {"title": "Risk-Level – Neu"}

class Update(SettingsUpdateView):
    model = RiskLevel
    fields = ["value", "label", "order", "active"]
    success_url = reverse_lazy("settingsapp:risklevel_list")
    extra_context = {"title": "Risk-Level – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = RiskLevel
    success_url = reverse_lazy("settingsapp:risklevel_list")
    extra_context = {"title": "Risk-Level – Löschen"}
