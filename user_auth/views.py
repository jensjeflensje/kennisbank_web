from django.shortcuts import  redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.conf import settings
from django.contrib import messages

from . import oauth
from . import models
from dashboard.models import Guild

TEMPLATE_PREFIX = "auth/"


def auth_login(request):
    if not request.user.is_authenticated:
        return redirect(settings.DC_AUTH_URI)
    return redirect("/dashboard/")


def auth_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def callback(request):
    token = oauth.get_token(request.GET["code"])
    if token:
        request.session["dc_token"] = token
        profile = oauth.get_route(token, "/users/@me")
        if profile:
            profile_obj = models.DiscordUser.objects.filter(userid=profile["id"]).first()
            if not profile_obj:
                user_obj = User(username=profile["id"])
                user_obj.save()
                profile_obj = models.DiscordUser(user=user_obj, userid=profile["id"], name=profile["username"])
                profile_obj.save()
            else:
                profile_obj.name = profile["username"]
            guild_data = oauth.get_route(token, "/users/@me/guilds")
            if guild_data:
                guild_data = [guild for guild in guild_data if guild["owner"]]
                for guild in guild_data:
                    if not Guild.objects.filter(discord_id=guild["id"]).first():
                        Guild(discord_id=guild["id"]).save()
                guild_list = [guild["id"] for guild in guild_data]
                request.session["guild_data"] = guild_data
                request.session["guild_list"] = guild_list
                login(request, profile_obj.user)
                request.session["username"] = profile_obj.name
                return redirect("/dashboard/")
            else:
                print("guilds")
        else:
            print("profile")
    else:
        print("token")
    messages.warning(request, "Oeps, er is iets fout gegaan.")
    return redirect("/")
