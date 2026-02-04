from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.permissions import SettingsAdminRequiredMixin

class SettingsListView(SettingsAdminRequiredMixin, ListView):
    template_name = "settingsapp/list.html"
    paginate_by = 50

class SettingsCreateView(SettingsAdminRequiredMixin, CreateView):
    template_name = "settingsapp/form.html"

class SettingsUpdateView(SettingsAdminRequiredMixin, UpdateView):
    template_name = "settingsapp/form.html"

class SettingsDeleteView(SettingsAdminRequiredMixin, DeleteView):
    template_name = "settingsapp/confirm_delete.html"
