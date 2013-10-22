from django import template
from django.conf import settings


register = template.Library()


@register.filter
def display_keyboard_icon(dummy):
    if hasattr(settings, 'HIDE_KEYBOARD_SHORTCUT_ICON') and settings.HIDE_KEYBOARD_SHORTCUT_ICON:
        return False
    return True
