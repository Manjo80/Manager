"""Split views by domain to keep things maintainable.

`recce.views` remains the stable import surface (wrapper module).
"""

from .vehicle import VehicleFilterView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView, VehicleDetailView
from .vehicle_photos import VehiclePhotoCreateView, VehiclePhotoDeleteView
from .install import InstallOptionCreateView, InstallOptionUpdateView, InstallOptionDeleteView, InstallOptionDetailView
from .install_photos import InstallPhotoCreateView, InstallPhotoDeleteView, InstallPhotoMarkersView, InstallPhotoMarkerDeleteView
from .fixed import FixedViewMarkersView, FixedViewMarkerDeleteView, FixedViewUpsertView
from .battery import BatteryConfigCreateView
from .setup import MaxSetupUpsertView, MaxSetupDeleteView

__all__ = [
    "VehicleFilterView",
    "VehicleCreateView",
    "VehicleUpdateView",
    "VehicleDeleteView",
    "VehicleDetailView",
    "VehiclePhotoCreateView",
    "VehiclePhotoDeleteView",
    "InstallOptionCreateView",
    "InstallOptionUpdateView",
    "InstallOptionDeleteView",
    "InstallOptionDetailView",
    "InstallPhotoCreateView",
    "InstallPhotoDeleteView",
    "InstallPhotoMarkersView",
    "InstallPhotoMarkerDeleteView",
    "FixedViewMarkersView",
    "FixedViewMarkerDeleteView",
    "FixedViewUpsertView",
    "BatteryConfigCreateView",
    "MaxSetupUpsertView",
    "MaxSetupDeleteView",
]
