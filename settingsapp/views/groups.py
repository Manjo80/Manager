from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import Group

class List(SettingsListView):
    model = Group
    extra_context = {"title": "Gruppen"}

class Create(SettingsCreateView):
    model = Group
    fields = ["name", "active"]
    success_url = reverse_lazy("settingsapp:group_list")
    extra_context = {"title": "Gruppen – Neu"}

class Update(SettingsUpdateView):
    model = Group
    fields = ["name", "active"]
    success_url = reverse_lazy("settingsapp:group_list")
    extra_context = {"title": "Gruppen – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = Group
    success_url = reverse_lazy("settingsapp:group_list")
    extra_context = {"title": "Gruppen – Löschen"}
