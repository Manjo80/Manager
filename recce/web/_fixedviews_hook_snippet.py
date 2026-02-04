"""
Drop-in snippet to integrate into recce/web/install.py.

1) Add import near the top of recce/web/install.py:

    from recce.services.fixed_views import ensure_fixed_views

2) In InstallOptionCreateView.form_valid (after the object is saved):

    response = super().form_valid(form)
    ensure_fixed_views(self.object)
    return response

3) In InstallOptionUpdateView.form_valid (after save):

    response = super().form_valid(form)
    ensure_fixed_views(self.object)
    return response

4) In InstallOptionDetailView.get_context_data (or dispatch/get):

    ensure_fixed_views(self.object)

That's it.
"""
