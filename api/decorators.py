from functools import wraps

from django.http import JsonResponse

from django.conf import settings


def api_key(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.GET.get("api_key") == settings.BOT_API_KEY:
            return function(request, *args, **kwargs)
            try:
                return function(request, *args, **kwargs)
            except KeyError as e:
                return JsonResponse({"success": False, "error": "Parameters missing: " + str(e)})
            except Exception as e:
                return JsonResponse({"success": False, "error": "Unknown error: " + str(e)})
        else:
            return JsonResponse({"success": False, "error": "Not authenticated."})

    return wrap
