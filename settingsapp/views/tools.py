from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import Tool

class List(SettingsListView):
    model = Tool
    extra_context = {"title": "Werkzeuge"}

class Create(SettingsCreateView):
    model = Tool
    fields = ["name", "photo", "active"]
    success_url = reverse_lazy("settingsapp:tool_list")
    extra_context = {"title": "Werkzeuge – Neu"}

class Update(SettingsUpdateView):
    model = Tool
    fields = ["name", "photo", "active"]
    success_url = reverse_lazy("settingsapp:tool_list")
    extra_context = {"title": "Werkzeuge – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = Tool
    success_url = reverse_lazy("settingsapp:tool_list")
    extra_context = {"title": "Werkzeuge – Löschen"}
