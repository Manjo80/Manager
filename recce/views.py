"""Backwards-compatible views module.

Internals live in recce.web.* to avoid one giant views.py.
Keep importing from `recce.views` in urls.py and other modules.
"""

from recce.web import *  # noqa: F401,F403
