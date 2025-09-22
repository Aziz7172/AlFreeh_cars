from django import template

register = template.Library()

@register.filter
def mod(value, arg):
    """Returns value modulo arg"""
    return (int(value) % int(arg))
