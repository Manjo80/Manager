from django.urls import path

from inventory.views.dashboard import DashboardView
from inventory.views.senders import (
    SenderListView, SenderCreateView, SenderUpdateView, SenderDeleteView
)
from inventory.views.status import SenderStatusUpdateView

app_name = "inventory"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),

    # Admin CRUD
    path("senders/", SenderListView.as_view(), name="sender_list"),
    path("senders/new/", SenderCreateView.as_view(), name="sender_new"),
    path("senders/<int:pk>/edit/", SenderUpdateView.as_view(), name="sender_edit"),
    path("senders/<int:pk>/delete/", SenderDeleteView.as_view(), name="sender_delete"),

    # Everyone (logged in): status only
    path("senders/<int:pk>/status/", SenderStatusUpdateView.as_view(), name="sender_status"),
]
