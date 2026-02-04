from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory.models import Sender
from inventory.forms.sender import SenderStatusForm

class SenderStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Sender
    form_class = SenderStatusForm
    template_name = "inventory/sender_status_form.html"
    success_url = reverse_lazy("inventory:dashboard")
