from django.db.models import Count, Q
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from inventory.models import Sender
from settingsapp.models import SenderModel


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["kpi"] = {
            "total": Sender.objects.count(),
            "available": Sender.objects.filter(status=Sender.Status.AVAILABLE).count(),
            "in_use": Sender.objects.filter(status=Sender.Status.IN_USE).count(),
            "defect": Sender.objects.filter(status=Sender.Status.DEFECT).count(),
            "lost": Sender.objects.filter(status=Sender.Status.LOST).count(),
        }

        ctx["available_by_group"] = (
            Sender.objects.filter(status=Sender.Status.AVAILABLE)
            .values("group__name")
            .annotate(count=Count("id"))
            .order_by("group__name")
        )
        ctx["available_without_group"] = Sender.objects.filter(
            status=Sender.Status.AVAILABLE, group__isnull=True
        )

        # Sender-Model Statistik: total + verfügbar
        ctx["sender_models_stats"] = (
            SenderModel.objects.filter(active=True)
            .annotate(
                total=Count("senders", distinct=True),
                available=Count(
                    "senders",
                    filter=Q(senders__status=Sender.Status.AVAILABLE),
                    distinct=True,
                ),
            )
            .filter(total__gt=0)
            .order_by("brand", "name")
        )

        return ctx
