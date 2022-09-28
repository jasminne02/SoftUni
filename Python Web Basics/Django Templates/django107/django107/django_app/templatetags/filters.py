from datetime import datetime

from django.template import Library


register = Library()


@register.filter('odd')
def odd(values):
    return [x for x in values if x % 2 == 1]
