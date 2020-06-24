from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages

from .models import Guild


def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            messages.warning(request, "Je moet eerst inloggen om dit te kunnen doen.")
            return redirect("/")

    return wrap


def get_guild_data(function):
    @wraps(function)
    def wrap(request, guild_id, *args, **kwargs):
        guild_data = None
        for guild in request.session["guild_data"]:
            if str(guild_id) == guild["id"]:
                guild_data = guild

        if not guild_data:
            messages.warning(request, "Deze guild bestaat niet.")
            return redirect("/dashboard/")
        return function(request, guild_id, guild_data, *args, **kwargs)

    return wrap


def get_guild_obj(function):
    @wraps(function)
    def wrap(request, guild_id, guild_data, *args, **kwargs):
        guild_obj = Guild.objects.get(discord_id=guild_id)
        return function(request, guild_id, guild_data, guild_obj, *args, **kwargs)

    return wrap


def is_guild_owner(function):
    @wraps(function)
    def wrap(request, guild_id, *args, **kwargs):
        if str(guild_id) in request.session["guild_list"]:
            return function(request, guild_id, *args, **kwargs)
        messages.warning(request, "Deze guild is niet van jou!")
        return redirect("/dashboard/")

    return wrap
