from __future__ import annotations

from typing import Iterable, List, Optional, TypeVar

from django.contrib import messages
from django.http import HttpRequest

T = TypeVar("T", bound=str)


def dedupe_case_insensitive(values: Iterable[str]) -> List[str]:
    """Unique strings, case-insensitive, stripped, sorted."""
    out: List[str] = []
    seen = set()
    for v in values:
        if not v:
            continue
        vv = v.strip()
        if not vv:
            continue
        key = vv.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(vv)
    out.sort(key=lambda s: s.casefold())
    return out


def try_import_sender_model():
    """Import SenderModel from settingsapp if available.

    Keeping this optional prevents the whole app failing to boot just because
    settingsapp moved/renamed during refactors. In the main project, it should exist.
    """
    try:
        from settingsapp.models import SenderModel  # type: ignore
        return SenderModel
    except Exception:
        return None


def require_sender_model(request: HttpRequest):
    SenderModel = try_import_sender_model()
    if SenderModel is None:
        messages.error(
            request,
            "SenderModel konnte nicht importiert werden. Prüfe settingsapp.models / INSTALLED_APPS.",
        )
    return SenderModel
