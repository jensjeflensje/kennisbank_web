from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages


def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            messages.warning(request, "Je moet eerst inloggen om dit te kunnen doen.")
            return redirect("/")

    return wrap
