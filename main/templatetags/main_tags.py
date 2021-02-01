import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time():
    return datetime.datetime.now().strftime("%I:%M %p")


@register.filter
def reverse(value):
    return "".join(value[::-1])
