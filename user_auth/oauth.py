import requests
from django.conf import settings
import base64


def get_token(code):
    data = {
        'client_id': settings.DC_CLIENT_ID,
        'client_secret': settings.DC_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.DC_REDIRECT_URI,
        'scope': 'identify guilds'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('https://discordapp.com/api/v6/oauth2/token', headers=headers, data=data)
    print(r.text)
    if r.status_code == 200:
        return r.json()["access_token"]
    return None


def get_route(token, route):
    headers = {
        "Authorization": "Bearer " + token
    }
    r = requests.get('https://discordapp.com/api/v6' + route, headers=headers)
    if r.status_code == 200:
        return r.json()
    return None
