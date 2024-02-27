from django import template

register = template.Library()

@register.filter
def delete_slash(url):
    return url.replace('/', '')