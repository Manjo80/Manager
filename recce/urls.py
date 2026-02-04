from django.urls import path
from recce import views

app_name = "recce"

urlpatterns = [
    path("", views.VehicleFilterView.as_view(), name="vehicle_filter"),
    path("vehicle/new/", views.VehicleCreateView.as_view(), name="vehicle_new"),
    path("vehicle/<int:pk>/", views.VehicleDetailView.as_view(), name="vehicle_detail"),
    path("vehicle/<int:pk>/edit/", views.VehicleUpdateView.as_view(), name="vehicle_edit"),
    path("vehicle/<int:pk>/delete/", views.VehicleDeleteView.as_view(), name="vehicle_delete"),

    path("vehicle/<int:vehicle_id>/photo/new/", views.VehiclePhotoCreateView.as_view(), name="vehicle_photo_new"),
    path("vehicle/photo/<int:pk>/delete/", views.VehiclePhotoDeleteView.as_view(), name="vehicle_photo_delete"),

    path("vehicle/<int:vehicle_id>/install/new/", views.InstallOptionCreateView.as_view(), name="install_new"),
    path("install/<int:pk>/", views.InstallOptionDetailView.as_view(), name="install_detail"),
    path("install/<int:pk>/edit/", views.InstallOptionUpdateView.as_view(), name="install_edit"),
    path("install/<int:pk>/delete/", views.InstallOptionDeleteView.as_view(), name="install_delete"),

    path("install/<int:install_id>/photo/new/", views.InstallPhotoCreateView.as_view(), name="install_photo_new"),
    path("install/photo/<int:pk>/delete/", views.InstallPhotoDeleteView.as_view(), name="install_photo_delete"),

    path("install/<int:install_id>/fixed/<str:view_type>/edit/", views.FixedViewUpsertView.as_view(), name="fixed_edit"),

    path("install/<int:install_id>/setup/new/", views.MaxSetupUpsertView.as_view(), name="setup_upsert"),
    path("setup/<int:pk>/delete/", views.MaxSetupDeleteView.as_view(), name="setup_delete"),


    path("install/photo/<int:pk>/markers/", views.InstallPhotoMarkersView.as_view(), name="install_photo_markers"),
    path("install/photo/marker/<int:pk>/delete/", views.InstallPhotoMarkerDeleteView.as_view(), name="install_photo_marker_delete"),

    path("fixed/<int:pk>/markers/", views.FixedViewMarkersView.as_view(), name="fixed_markers"),
    path("fixed/marker/<int:pk>/delete/", views.FixedViewMarkerDeleteView.as_view(), name="fixed_marker_delete"),

    path("batteryconfig/new/", views.BatteryConfigCreateView.as_view(), name="batteryconfig_new"),
]
