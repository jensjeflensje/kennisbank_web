from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Guild, Question, GuildChannel
from .decorators import login_required, get_guild_data, is_guild_owner, get_guild_obj
from .forms import QuestionForm, ChannelForm

TEMPLATE_PREFIX = "dashboard/"


@login_required
def home(request):
    return render(request, TEMPLATE_PREFIX + "index.html")


@login_required
@get_guild_data
@is_guild_owner
@get_guild_obj
def view_guild(request, guild_id, guild_data, guild_obj):
    questions = Question.objects.filter(guild=guild_obj).all()
    channels = GuildChannel.objects.filter(guild=guild_obj).all()
    context = {
        "guild_data": guild_data,
        "questions": questions,
        "channels": channels,
    }
    return render(request, TEMPLATE_PREFIX + "view_guild.html", context)


@login_required
@is_guild_owner
@get_guild_data
@get_guild_obj
def add_question(request, guild_id, guild_data, guild_obj):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guild_id = guild_obj.id
            obj.save()
            messages.success(request, "Vraag succesvol toegevoegd!")
            return redirect(f"/dashboard/{guild_id}/")
    else:
        form = QuestionForm()
    context = {
        "guild_data": guild_data,
        "form": form
    }
    return render(request, TEMPLATE_PREFIX + "view_guild_questions.html", context)


@login_required
@is_guild_owner
@get_guild_data
@get_guild_obj
def edit_question(request, guild_id, guild_data, guild_obj, question_id=0):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guild_id = guild_obj.id
            obj.save()
            messages.success(request, "Vraag succesvol bewerkt!")
    else:
        form = QuestionForm(instance=question)
    context = {
        "guild_data": guild_data,
        "form": form
    }
    return render(request, TEMPLATE_PREFIX + "view_guild_questions_edit.html", context)


@login_required
@is_guild_owner
@get_guild_data
@get_guild_obj
def delete_question(request, guild_id, guild_data, guild_obj, question_id=0):
    question = get_object_or_404(Question, pk=question_id, guild=guild_obj)
    question.delete()
    messages.success(request, "Vraag succesvol verwijderd!")
    return redirect(f"/dashboard/{guild_id}/")


@login_required
@is_guild_owner
@get_guild_data
@get_guild_obj
def add_channel(request, guild_id, guild_data, guild_obj):
    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guild_id = guild_obj.id
            obj.save()
            messages.success(request, "Kanaal succesvol toegevoegd!")
            return redirect(f"/dashboard/{guild_id}/")
    else:
        form = ChannelForm()
    context = {
        "guild_data": guild_data,
        "form": form
    }
    return render(request, TEMPLATE_PREFIX + "view_guild_channels.html", context)


@login_required
@is_guild_owner
@get_guild_data
@get_guild_obj
def edit_channel(request, guild_id, guild_data, guild_obj, channel_id=0):
    channel = get_object_or_404(GuildChannel, pk=channel_id, guild=guild_obj)
    if request.method == "POST":
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guild_id = guild_obj.id
            obj.save()
            messages.success(request, "Kanaal succesvol bewerkt!")
    else:
        form = ChannelForm(instance=channel)
    context = {
        "guild_data": guild_data,
        "form": form
    }
    return render(request, TEMPLATE_PREFIX + "view_guild_channels_edit.html", context)


@login_required
@is_guild_owner
@get_guild_data
@get_guild_obj
def delete_channel(request, guild_id, guild_data, guild_obj, channel_id=0):
    channel = get_object_or_404(GuildChannel, pk=channel_id)
    channel.delete()
    messages.success(request, "Kanaal succesvol verwijderd!")
    return redirect(f"/dashboard/{guild_id}/")
