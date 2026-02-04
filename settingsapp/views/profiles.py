from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import Profile

class List(SettingsListView):
    model = Profile
    extra_context = {"title": "Profile"}

class Create(SettingsCreateView):
    model = Profile
    fields = ["name", "active"]
    success_url = reverse_lazy("settingsapp:profile_list")
    extra_context = {"title": "Profile – Neu"}

class Update(SettingsUpdateView):
    model = Profile
    fields = ["name", "active"]
    success_url = reverse_lazy("settingsapp:profile_list")
    extra_context = {"title": "Profile – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = Profile
    success_url = reverse_lazy("settingsapp:profile_list")
    extra_context = {"title": "Profile – Löschen"}
