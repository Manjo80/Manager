from django.urls import reverse_lazy
from settingsapp.views.common import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView
from settingsapp.models import ReccePerspective

class List(SettingsListView):
    model = ReccePerspective
    extra_context = {"title": "Recce Perspektiven"}

class Create(SettingsCreateView):
    model = ReccePerspective
    fields = ["key", "label", "order", "active"]
    success_url = reverse_lazy("settingsapp:recceperspective_list")
    extra_context = {"title": "Recce Perspektiven – Neu"}

class Update(SettingsUpdateView):
    model = ReccePerspective
    fields = ["key", "label", "order", "active"]
    success_url = reverse_lazy("settingsapp:recceperspective_list")
    extra_context = {"title": "Recce Perspektiven – Bearbeiten"}

class Delete(SettingsDeleteView):
    model = ReccePerspective
    success_url = reverse_lazy("settingsapp:recceperspective_list")
    extra_context = {"title": "Recce Perspektiven – Löschen"}
