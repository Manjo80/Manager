from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.permissions import InventoryAdminRequiredMixin
from inventory.models import Sender
from inventory.forms import SenderAdminForm


class SenderListView(InventoryAdminRequiredMixin, ListView):
    model = Sender
    template_name = "inventory/sender_list.html"
    paginate_by = 50
    ordering = ["name"]


class SenderCreateView(InventoryAdminRequiredMixin, CreateView):
    model = Sender
    form_class = SenderAdminForm
    template_name = "inventory/sender_form.html"
    success_url = reverse_lazy("inventory:sender_list")


class SenderUpdateView(InventoryAdminRequiredMixin, UpdateView):
    model = Sender
    form_class = SenderAdminForm
    template_name = "inventory/sender_form.html"
    success_url = reverse_lazy("inventory:sender_list")


class SenderDeleteView(InventoryAdminRequiredMixin, DeleteView):
    model = Sender
    template_name = "inventory/confirm_delete.html"
    success_url = reverse_lazy("inventory:sender_list")
