from functools import wraps
from django.http import HttpResponseForbidden

def roles_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.pvdmusers1.role.name in roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to view this page.")
        return _wrapped_view
    return decorator