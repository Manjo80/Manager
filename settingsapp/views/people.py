from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import Person

class List(SettingsListView):
    model = Person
    extra_context = {"title": "Personen"}

class Create(SettingsCreateView):
    model = Person
    fields = ["short", "codename", "active"]
    success_url = reverse_lazy("settingsapp:person_list")
    extra_context = {"title": "Personen – Neu"}

class Update(SettingsUpdateView):
    model = Person
    fields = ["short", "codename", "active"]
    success_url = reverse_lazy("settingsapp:person_list")
    extra_context = {"title": "Personen – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = Person
    success_url = reverse_lazy("settingsapp:person_list")
    extra_context = {"title": "Personen – Löschen"}
