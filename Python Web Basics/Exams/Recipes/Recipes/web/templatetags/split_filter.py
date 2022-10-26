from django import template

register = template.Library()


@register.filter(name='split')
def split(string: str, element):
    """ Returns a value split by an element """
    return string.split(element)
