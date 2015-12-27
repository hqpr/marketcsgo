from django.shortcuts import render
import random
from django.conf import settings
import urllib2
import json

from apps.account.models import UserProfile

AGENT = settings.AGENT
SLEEP = settings.BOT_SLEEP
DOMAIN = settings.MARKET_DOMAIN

def home(request):
    try:
        user = UserProfile.objects.get(user=request.user)
        api_key = user.api_key
        steam = user.steam_username
    except UserProfile.DoesNotExist:
        pass
    data = {}
    return render(request, 'index.html', data)
