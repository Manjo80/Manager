from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class GroupRequiredMixin(LoginRequiredMixin):
    """Require membership in a specific Django group (or superuser)."""
    required_group = None  # set in subclasses

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not self.required_group:
            raise PermissionDenied("required_group not set")

        if not request.user.groups.filter(name=self.required_group).exists():
            raise PermissionDenied("no access")

        return super().dispatch(request, *args, **kwargs)


class SettingsAdminRequiredMixin(GroupRequiredMixin):
    """Only users in group 'settings_access' (or superuser) may access settings."""
    required_group = "settings_access"


class InventoryAdminRequiredMixin(GroupRequiredMixin):
    """Only users in group 'inventory_admin' (or superuser) may fully manage inventory."""
    required_group = "inventory_admin"
