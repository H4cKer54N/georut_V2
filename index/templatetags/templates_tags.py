from django import template

register = template.Library()

@register.filter
def delete_slash(url):
    return url.replace('/', '')

@register.filter
def check_permissions(user,permission):
    return user.groups.filter(permissions__codename=permission).exists()