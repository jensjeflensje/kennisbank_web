from django.http import JsonResponse

from dashboard.models import GuildChannel, Question
from .decorators import api_key
from .utils import find_question

import time


@api_key
def get_used_channels(request):
    channels = GuildChannel.objects.all()
    channels_sorted = {}
    for channel in channels:
        if not channels_sorted.get(channel.guild.discord_id):
            channels_sorted[channel.guild.discord_id] = []
        channels_sorted[channel.guild.discord_id].append(channel.channel_id)
    return JsonResponse({"success": True, "data": channels_sorted})


@api_key
def get_answer(request):
    time1 = time.time()
    question = request.GET["question"]
    guild = request.GET["guild"]
    possible_answers = Question.objects.filter(guild__discord_id=guild).all()
    found_answer = find_question(question, possible_answers)
    if found_answer:
        time2 = time.time()
        return JsonResponse({"success": True, "data": found_answer.serialize(), "time": time2 - time1})
    else:
        return JsonResponse({"success": False, "error": "No question found."})
