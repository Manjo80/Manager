from django import template

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    if user is None or not getattr(user, "is_authenticated", False):
        return False
    if getattr(user, "is_superuser", False):
        return True
    return user.groups.filter(name=group_name).exists()
