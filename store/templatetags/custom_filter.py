
from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        return f"£  {value:,.2f}"
    except (ValueError, TypeError):
        return value

@register.filter(name='multiply')
def multiply(value, multiplier):
    try:
        return value * multiplier
    except (ValueError, TypeError):
        return value