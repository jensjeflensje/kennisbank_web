from django.http import JsonResponse

from dashboard.models import GuildChannel, Question
from .decorators import api_key
from .utils import find_question


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
    question = request.GET["question"]
    guild = request.GET["guild"]
    possible_answers = Question.objects.filter(guild__discord_id=guild).all()
    print(possible_answers)
    found_answer = find_question(question, possible_answers)
    if found_answer:
        return JsonResponse({"success": True, "data": found_answer.serialize()})
    else:
        return JsonResponse({"success": False, "error": "No question found."})
