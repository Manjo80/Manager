from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import SenderModel

class List(SettingsListView):
    model = SenderModel
    extra_context = {"title": "Sender-Modelle"}

class Create(SettingsCreateView):
    model = SenderModel
    fields = ["brand", "name", "photo", "has_audio", "has_fixed_power", "supported_batteries", "profiles", "active"]
    success_url = reverse_lazy("settingsapp:sendermodel_list")
    extra_context = {"title": "Sender-Modelle – Neu"}

class Update(SettingsUpdateView):
    model = SenderModel
    fields = ["brand", "name", "photo", "has_audio", "has_fixed_power", "supported_batteries", "profiles", "active"]
    success_url = reverse_lazy("settingsapp:sendermodel_list")
    extra_context = {"title": "Sender-Modelle – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = SenderModel
    success_url = reverse_lazy("settingsapp:sendermodel_list")
    extra_context = {"title": "Sender-Modelle – Löschen"}
