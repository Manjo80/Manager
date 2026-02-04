from django import forms
from inventory.models import Sender


class SenderAdminForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = ["name", "phone_number", "model", "status", "group", "note"]


class SenderStatusForm(forms.ModelForm):
    """Status update for normal users.
    Rule:
      - If status == AVAILABLE, group must be set.
      - If status != AVAILABLE, group is cleared.
    """

    class Meta:
        model = Sender
        fields = ["status", "group"]

    def clean(self):
        cleaned = super().clean()
        status = cleaned.get("status")
        group = cleaned.get("group")

        if status == Sender.Status.AVAILABLE and group is None:
            self.add_error("group", "Gruppe ist erforderlich, wenn der Sender verfügbar ist.")
        if status != Sender.Status.AVAILABLE:
            cleaned["group"] = None
        return cleaned
