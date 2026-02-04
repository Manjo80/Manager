"""Public model exports for the recce app.

Rule: other modules import models via `recce.models`.

This file must be **boring and stable**. Import defensively to avoid Django
startup failing when internal modules are refactored.
"""

# Vehicle
from .vehicle import RecceVehicle, VehiclePhoto

# Install flow
from .install import InstallFixedView, InstallOption, InstallPhoto

# Compat / setup
from .compat import BatteryConfig, InstallOptionMaxSetup

# Markers
from .markers import FixedViewMarker, InstallPhotoMarker

# Cross-app (settings) models – optional
try:
    from settingsapp.models.batteries import BatteryType  # type: ignore
except Exception:  # pragma: no cover
    BatteryType = None  # type: ignore

__all__ = [
    "RecceVehicle",
    "VehiclePhoto",
    "InstallOption",
    "InstallPhoto",
    "InstallFixedView",
    "BatteryConfig",
    "InstallOptionMaxSetup",
    "FixedViewMarker",
    "InstallPhotoMarker",
    "BatteryType",
]
