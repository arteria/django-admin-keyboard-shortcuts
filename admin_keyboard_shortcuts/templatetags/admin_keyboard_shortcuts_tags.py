from django import template
from django.conf import settings


register = template.Library()


@register.filter
def display_cmd_key_icon(dummy):
    if hasattr(settings, 'ADMIN_KEYBOARD_SHORTCUTS_HIDE_ICON') and settings.ADMIN_KEYBOARD_SHORTCUTS_HIDE_ICON:
        return False
    return True
