from django.http import HttpResponseNotFound
from django.shortcuts import render
from functools import wraps

def check_permissions_view(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(permissions__codename=permission).exists():
                return view_func(request, *args, **kwargs)
            else:
                return render(request, '404.html', status=404)
        return _wrapped_view
    return decorator