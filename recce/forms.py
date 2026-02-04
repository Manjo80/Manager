"""Backwards-compatible forms module.

Internals live in recce.ui_forms.* to avoid one giant forms.py.
Keep importing from `recce.forms` in the rest of the project.
"""

from recce.ui_forms import *  # noqa: F401,F403
