#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
import urllib2
import json
import time

from apps.account.models import UserProfile

AGENT = settings.AGENT
SLEEP = settings.BOT_SLEEP
DOMAIN = settings.MARKET_DOMAIN

def home(request):
    try:
        user = UserProfile.objects.get(user=request.user)
        api_key = '?key=%s' % user.api_key
        steam = user.steam_username

        steamcommunity = 'http://steamcommunity.com/profiles/%s/inventory/json/730/2/' % steam
        response = urllib2.urlopen(steamcommunity)
        data = json.load(response)
        inv_len = len(data['rgInventory'])

        len_current_trade = 0
        current_trade = {}
        url = '%s/api/Trades/%s' % (DOMAIN, api_key)
        data = get_request(url)
        for d in data:
            item_id = '%s_%s' % (d['i_classid'], d['i_instanceid'])
            current_trade.update({item_id: [{'price': d['ui_price']},
                                            {'min_price': d['min_price']},
                                            {'market_price': d['i_market_price']},
                                            {'name': d['i_name']},
                                            {'id': d['ui_id']}]})
            len_current_trade += 1
        print 'Items in trade: %d' % len_current_trade

    except UserProfile.DoesNotExist:
        api_key = None
        steam = None
        inv_len = None
        len_current_trade = 0

    data = {'api_key': api_key,
            'steam': steam,
            'inv_len': inv_len,
            'len_current_trade': len_current_trade}
    return render(request, 'index.html', data)


def get_request(url):
    request = urllib2.Request(url, None, {'User-agent': AGENT})
    response = urllib2.urlopen(request)
    time.sleep(SLEEP)
    return json.load(response)


def inventory(request):
    try:
        user = UserProfile.objects.get(user=request.user)
        steamcommunity = 'http://steamcommunity.com/profiles/%s/inventory/json/730/2/' % user.steam_username
        response = urllib2.urlopen(steamcommunity)
        data = json.load(response)
        inventory = data['rgInventory']

    except UserProfile.DoesNotExist:
        inventory = None

    data = {'inventory': inventory}
    return render(request, 'inventory.html', data)
