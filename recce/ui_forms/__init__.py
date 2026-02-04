"""Forms are split by domain to keep imports stable and errors local."""

from .vehicle import VehicleForm, VehiclePhotoForm
from .install import InstallOptionForm, InstallPhotoForm, FixedViewForm
from .markers import InstallPhotoMarkerForm, FixedViewMarkerForm
from .battery import BatteryConfigForm
from .setup import MaxSetupForm

__all__ = [
    "VehicleForm",
    "VehiclePhotoForm",
    "InstallOptionForm",
    "InstallPhotoForm",
    "FixedViewForm",
    "BatteryConfigForm",
    "MaxSetupForm",
    "InstallPhotoMarkerForm",
    "FixedViewMarkerForm",
]
