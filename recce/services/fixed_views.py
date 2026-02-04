from __future__ import annotations

from typing import Iterable

from django.db import transaction


DEFAULT_VIEW_TYPES: tuple[str, ...] = ("front", "rear", "side", "top")


def _get_fixed_view_model():
    """Locate the FixedView model across common refactor layouts."""
    # Newer refactor layout
    try:
        from recce.models.fixed_view import FixedView  # type: ignore
        return FixedView
    except Exception:
        pass

    # Common legacy name
    try:
        from recce.models.install import InstallFixedView  # type: ignore
        return InstallFixedView
    except Exception:
        pass

    # Fallback: if re-exported
    try:
        from recce.models import FixedView  # type: ignore
        return FixedView
    except Exception:
        pass

    raise ImportError(
        "Could not locate FixedView model. Expected recce.models.fixed_view.FixedView or recce.models.install.InstallFixedView."
    )


def _get_install_fk_field(FixedViewModel):
    """Find FK field on FixedView that points to InstallOption."""
    for f in FixedViewModel._meta.get_fields():
        if not getattr(f, "is_relation", False):
            continue
        if getattr(f, "many_to_one", False) and getattr(f, "related_model", None) is not None:
            rm = f.related_model
            if rm and rm.__name__ in ("InstallOption", "Installoption"):
                return f.name

    # Fallback to common names
    field_names = [f.name for f in FixedViewModel._meta.get_fields()]
    for candidate in ("install_option", "install"):
        if candidate in field_names:
            return candidate

    raise RuntimeError("Could not determine FK field from FixedView -> InstallOption.")


@transaction.atomic
def ensure_fixed_views(install, view_types: Iterable[str] = DEFAULT_VIEW_TYPES) -> None:
    """Ensure 4 standard fixed views exist for an InstallOption (idempotent)."""
    FixedViewModel = _get_fixed_view_model()
    fk_name = _get_install_fk_field(FixedViewModel)

    for vt in view_types:
        vt = str(vt).lower().strip()
        if not vt:
            continue
        kwargs = {fk_name: install, "view_type": vt}
        FixedViewModel.objects.get_or_create(**kwargs)
