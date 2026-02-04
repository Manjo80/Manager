from django.urls import path
from django.views.generic import TemplateView

from settingsapp.views import people, tools, batteries, profiles, sender_models, groups, recce_perspectives, risk_levels

app_name = "settingsapp"

urlpatterns = [
    path("", TemplateView.as_view(template_name="settingsapp/index.html"), name="index"),

    path("people/", people.List.as_view(), name="person_list"),
    path("people/new/", people.Create.as_view(), name="person_create"),
    path("people/<int:pk>/edit/", people.Update.as_view(), name="person_update"),
    path("people/<int:pk>/delete/", people.Delete.as_view(), name="person_delete"),

    path("tools/", tools.List.as_view(), name="tool_list"),
    path("tools/new/", tools.Create.as_view(), name="tool_create"),
    path("tools/<int:pk>/edit/", tools.Update.as_view(), name="tool_update"),
    path("tools/<int:pk>/delete/", tools.Delete.as_view(), name="tool_delete"),

    path("batteries/", batteries.List.as_view(), name="batterytype_list"),
    path("batteries/new/", batteries.Create.as_view(), name="batterytype_create"),
    path("batteries/<int:pk>/edit/", batteries.Update.as_view(), name="batterytype_update"),
    path("batteries/<int:pk>/delete/", batteries.Delete.as_view(), name="batterytype_delete"),

    path("profiles/", profiles.List.as_view(), name="profile_list"),
    path("profiles/new/", profiles.Create.as_view(), name="profile_create"),
    path("profiles/<int:pk>/edit/", profiles.Update.as_view(), name="profile_update"),
    path("profiles/<int:pk>/delete/", profiles.Delete.as_view(), name="profile_delete"),

    path("sender-models/", sender_models.List.as_view(), name="sendermodel_list"),
    path("sender-models/new/", sender_models.Create.as_view(), name="sendermodel_create"),
    path("sender-models/<int:pk>/edit/", sender_models.Update.as_view(), name="sendermodel_update"),
    path("sender-models/<int:pk>/delete/", sender_models.Delete.as_view(), name="sendermodel_delete"),

    path("groups/", groups.List.as_view(), name="group_list"),
    path("groups/new/", groups.Create.as_view(), name="group_create"),
    path("groups/<int:pk>/edit/", groups.Update.as_view(), name="group_update"),
    path("groups/<int:pk>/delete/", groups.Delete.as_view(), name="group_delete"),

    path("recce-perspectives/", recce_perspectives.List.as_view(), name="recceperspective_list"),
    path("recce-perspectives/new/", recce_perspectives.Create.as_view(), name="recceperspective_create"),
    path("recce-perspectives/<int:pk>/edit/", recce_perspectives.Update.as_view(), name="recceperspective_update"),
    path("recce-perspectives/<int:pk>/delete/", recce_perspectives.Delete.as_view(), name="recceperspective_delete"),

    path("risk-levels/", risk_levels.List.as_view(), name="risklevel_list"),
    path("risk-levels/new/", risk_levels.Create.as_view(), name="risklevel_create"),
    path("risk-levels/<int:pk>/edit/", risk_levels.Update.as_view(), name="risklevel_update"),
    path("risk-levels/<int:pk>/delete/", risk_levels.Delete.as_view(), name="risklevel_delete"),
]
