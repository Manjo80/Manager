from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth (login/logout) – include ONCE to avoid duplicate namespace warnings
    path("", include(("accounts.urls", "accounts"), namespace="accounts")),

    path("", include("inventory.urls")),
    path("", include("recce.urls")),
    path("settings/", include("settingsapp.urls")),
]
