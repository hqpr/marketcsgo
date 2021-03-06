#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
from django.conf import settings
import urllib2
import json
import csv
import simplejson

from apps.account.models import UserProfile
from marketcsgo.views import get_request


def db_filename():
    url = '%s/itemdb/current_730.json' % settings.MARKET_DOMAIN
    data = get_request(url)
    return data['db']


def update_db(file_name):
    url = '%s/itemdb/%s' % (settings.MARKET_DOMAIN, file_name)
    fp = open(settings.LOCAL_DB, 'wb+')
    req = urllib2.Request(url, None, {'User-agent': settings.AGENT})
    resp = urllib2.urlopen(req)
    content = resp.read()
    fp.write(content)


def find_in_db(q):
    reader = csv.reader(open(settings.LOCAL_DB, 'rb+'), delimiter=';', quotechar='"')
    try:
        q = q.replace(' | ', ' ')
        q_quality = q.split('(')[1].replace(')', '')
        q = q.split('(')[0]
        for row in reader:
            name = row[9].replace(' | ', ' ')
            name = name.split('(')[0]
            name = name.decode('utf-8')
            name = name.replace(u'Райский страж', 'Heaven Guard')
            name = name.replace(u'Пучина', 'Abyss')
            name = name.replace(u'Смокинг', 'Tuxedo')
            name = name.replace(u'Городская опасность', 'Urban Hazard')
            name = name.replace(u'Хищник', 'Predator')
            name = name.replace(u'Ночь', 'Night')
            name = name.replace(u'Латунь', 'Brass')
            name = name.replace(u'Синяя трещина', 'Blue Fissure')
            name = name.replace(u'Кислотный градиент', 'Acid Fade')
            name = name.replace(u'Африканская сетка', 'Safari Mesh')
            name = name.replace(u'Нержавейка', 'Stainless')
            name = name.replace(u'Жар', 'Heat')
            name = name.replace(u'Осирис', 'Osiris')
            name = name.replace(u'Лабиринт', 'Labyrinth')
            name = name.replace(u'Янтарный градиент', 'Amber Fade')
            name = name.replace(u'Валентность', 'Valence')
            name = name.replace(u'Жернов', 'Grinder')
            name = name.replace(u'Страж', 'Guardian')
            name = name.replace(u'Грифон', 'Griffin')
            name = name.replace(u'Метеорит', 'Meteorite')
            name = name.replace(u'Грунтовая вода', 'Groundwater')
            name = name.replace(u'Кёльн', 'Cologne')
            name = name.replace(u'Цвет джунглей', 'Jungle Spray')
            name = name.replace(u'Смешанный камуфляж', 'VariCamo')
            name = name.replace(u'Калифорнийский камуфляж', 'CaliCamo')
            name = name.replace(u'Гадюка', 'Pit Viper')
            name = name.replace(u'Гексан', 'Hexane')
            name = name.replace(u'Когти', 'Slashed')
            name = name.replace(u'Кровавая паутина', 'Crimson Web')
            name = name.replace(u'Карамельное яблоко', 'Candy Apple')
            name = name.replace(u'Смерч', 'Tornado')
            name = name.replace(u'Песчаная буря', 'Desert Storm')
            name = name.replace(u'Пульс', 'Pulse')
            name = name.replace(u'Франклин', 'Franklin')
            name = name.replace(u'Демонтаж', 'Teardown')
            name = name.replace(u'Паслен', 'Nightshade')
            name = name.replace(u'Охотничья будка', 'Hunting Blind')
            name = name.replace(u'Разбойник', 'Highwayman')
            name = name.replace(u'Осадок', 'Mudder')
            name = name.replace(u'Причал', 'Marina')
            name = name.replace(u'Лихач', 'Hot Shot')
            name = name.replace(u'Сержант', 'Sergeant')
            name = name.replace(u'Карп кои', 'Koi')
            name = name.replace(u'Пантера', 'Pantera')
            name = name.replace(u'Сверхновая', 'Supernova')
            name = name.replace(u'Песчаные дюны', 'Sand Dune')
            name = name.replace(u'Зеленое яблоко', 'Green Apple')
            name = name.replace(u'Красный кварц', 'Red Quartz')
            name = name.replace(u'Пассажир', 'Commuter')
            name = name.replace(u'Колония', 'Colony')
            name = name.replace(u'Элитное снаряжение', 'Elite Build')
            name = name.replace(u'Почва', 'Terrain')
            name = name.replace(u'Анодированная синева', 'Anodized Navy')
            name = name.replace(u'Айзек', 'Isaac')
            name = name.replace(u'Луговые листья', 'Grassland Leaves')
            name = name.replace(u'Пиксельный камуфляж «Город»', 'Urban DDPAT')
            name = name.replace(u'Гемоглобин', 'Hemoglobin')
            name = name.replace(u'Пороховой дым', 'Gunsmoke')
            name = name.replace(u'Ками', 'Kami')
            name = name.replace(u'Синий ламинат', 'Blue Laminate')
            name = name.replace(u'Спокойствие', 'Tranquility')
            name = name.replace(u'Пустынная атака', 'Desert Strike')
            name = name.replace(u'Василиск', 'Basilisk')
            name = name.replace(u'Реактор', 'Reactor')
            name = name.replace(u'Атомный сплав', 'Atomic Alloy')
            name = name.replace(u'Кровавая паутина', 'Crimson Web')
            name = name.replace(u'Птичьи игры', 'Fowl Play')
            name = name.replace(u'Заговор', 'Conspiracy')
            name = name.replace(u'Частица титана', 'Titanium Bit')
            name = name.replace(u'Картель', 'Cartel')
            name = name.replace(u'Изумрудные завитки', 'Emerald Pinstripe')
            name = name.replace(u'Водяной', 'Water Elemental')
            name = name.replace(u'Хамелеон', 'Chameleon')
            name = name.replace(u'Королевский синий', 'Royal_Blue')
            name = name.replace(u'Проклятие', 'Curse')
            name = name.replace(u'Ржавая сталь', 'Steel Disruption')
            name = name.replace(u'Восходящий череп', 'Rising Skull')
            name = name.replace(u'Заблуждение', 'Delusion')
            name = name.replace(u'Серебряный кварц', 'Silver Quartz')
            name = name.replace(u'Городской щебень', 'Urban Rubble')
            name = name.replace(u'Слоновая кость', 'Ivory')
            name = name.replace(u'Красная линия', 'Redline')
            name = name.replace(u'Джунгли', 'Jungle')
            name = name.replace(u'Сайрекс', 'Cyrex')
            name = name.replace(u'Ночные операции', 'Night Ops')
            name = name.replace(u'Костяная маска', 'Bone Mask')
            name = name.replace(u'Покойник', 'Muertos')
            name = name.replace(u'Улей', 'Hive')
            name = name.replace(u'Цвета прибоя', 'Undertow')
            name = name.replace(u'Камуфляж', 'VariCamo')
            name = name.replace(u'Красный глянец', 'Red Laminate')
            name = name.replace(u'Тигр', 'Tigris')
            name = name.replace(u'Медная галактика', 'Copper Galaxy')
            name = name.replace(u'Красные фрагменты', 'Red FragCam')
            name = name.replace(u'Радиоактивные осадки', 'Fallout Warning')
            name = name.replace(u'Король драконов', 'Dragon King')
            name = name.replace(u'Горелка Бунзена', 'Bunsen Burner')
            name = name.replace(u'Поверхностная закалка', 'Case Hardened')
            name = name.replace(u'Слепое пятно', 'Blind Spot')
            name = name.replace(u'Пустынная атака', 'Desert-Strike')
            name = name.replace(u'Гипнотический', 'Hypnotic')
            name = name.replace(u'Грецкий орех', 'Firestarter')
            name = name.replace(u'Поджигатель', 'Hypnotic')
            name = name.replace(u'Вирус', 'Virus')
            name = name.replace(u'Чайка', 'Seabird')
            name = name.replace(u'Тусклые полосы', 'Faded Zebra')

            name = name.replace(u'Синий титан', 'Blue Titanium')
            name = name.replace(u'Модуль', 'Module')
            name = name.replace(u'Кортисейра', 'Corticera')

            name = name.replace(u'Листовая сталь', 'Tread Plate')
            name = name.replace(u'Кровавый тигр', 'Blood Tiger')

            if q in name:
                db_quality = row[6].decode('utf-8')
                db_quality = db_quality.replace(u'Немного поношенное', 'Minimal Wear')
                db_quality = db_quality.replace(u'Закаленное в боях', 'Battle-Scarred)')
                db_quality = db_quality.replace(u'Поношенное', 'Well-Worn')
                db_quality = db_quality.replace(u'После полевых испытаний', 'Field-Tested)')
                db_quality = db_quality.replace(u'Прямо с завода', 'Factory New')
                if q_quality in db_quality:
                    # print '%s= %s, set=%s' % (name, db_quality, int(row[2]) - 1)
                    return int(row[2]) - 1
    except IndexError:
        pass


def set_price(item, price, api_key):
    url = '%s/api/SetPrice/%s/%s/%s' % (settings.MARKET_DOMAIN, item, price, api_key)
    data = get_request(url)
    print
    if data['success'] and 'position' in data:
        print 'Success: %s, Position: %s' % (data['success'], data['position'])
    else:
        print data


def process_item(item, api_key, debug_mode):

    def set_new_price(item, price):
        url = '%s/api/SetPrice/new_%s/%s/%s' % (settings.MARKET_DOMAIN, item, price, api_key)
        data = get_request(url)
        print
        if 'position' in data:
            print 'Success: %s, Position: %s' % (data['success'], data['position'])

    msg = []
    try:

        current_trade = {}
        url = '%s/api/Trades/%s' % (settings.MARKET_DOMAIN, api_key)
        data = get_request(url)
        for d in data:
            item_id = '%s_%s' % (d['i_classid'], d['i_instanceid'])
            current_trade.update({item_id: [{'price': d['ui_price']},
                                            {'min_price': d['min_price']},
                                            {'market_price': d['i_market_price']},
                                            {'name': d['i_name']},
                                            {'id': d['ui_id']}]})
        my_trade = current_trade
        item_id = '%s_%s' % (item['classid'], item['instanceid'])
        market_name = item['market_hash_name']
        item_name = item['name']
        if item['min_price'] == -1:
            if find_in_db(market_name):
                if item_id not in my_trade:
                    if not debug_mode:
                        set_new_price(item_id, find_in_db(market_name))
                    result = '[*] %s = %s\n' % (item_name, find_in_db(market_name))
                    msg.append(result)
            else:
                if item_id not in my_trade:
                    if not debug_mode:
                        set_new_price(item_id, 5000000)
                    result = '[*] %s = %s\n' % (item_name, 5000000)
                    msg.append(result)
        else:
            # Все нашло, ставим на 1 коп меньше
            updated_price = int(item['min_price']) - 1
            if item_id not in my_trade:
                if not debug_mode:
                    set_new_price(item_id, updated_price)
                result = '[+] %s = %s\n' % (item_name, updated_price)
                msg.append(result)
    except Exception as e:
        pass
        # print item
        print e
    return msg


def update(request):
    if request.method == 'POST':
        resp = {}
        msg = []
        try:
            user = UserProfile.objects.get(user=request.user)
            api_key = '?key=%s' % user.api_key
            debug_mode = user.debug_mode

            url = '%s/api/Trades/%s' % (settings.MARKET_DOMAIN, api_key)
            data = get_request(url)
            for d in data:

                item = '%s' % d['ui_id']

                our_price = int('{:.0f}'.format(float(d['ui_price'])*100))
                rec_price = int('{:.0f}'.format(float(d['i_market_price'])*100))
                min_price = int('{:.0f}'.format(float(d['min_price'])*100))
                name = d['i_name']
                abs_min_price = int('{:.0f}'.format(round(rec_price*0.7)))

                updated_price = our_price + 1
                condition = 0

                if our_price < min_price < rec_price:
                    updated_price = min_price - 1
                    condition = 1

                if our_price > min_price < rec_price:
                    updated_price = min_price - 1
                    condition = 2

                if rec_price and our_price >= min_price > rec_price:
                    updated_price = rec_price
                    condition = 3

                if rec_price and our_price < min_price > rec_price:
                    updated_price = rec_price
                    condition = 4

                if not rec_price and our_price < min_price:
                    updated_price = min_price - 1
                    condition = 5

                if not rec_price and our_price > min_price:
                    updated_price = min_price - 1
                    condition = 6

                if not min_price and rec_price and our_price >= rec_price:
                    updated_price = rec_price
                    condition = 7

                if not min_price and not rec_price and our_price > rec_price:
                    updated_price = our_price
                    condition = 8

                if not rec_price and min_price and our_price > min_price:
                    updated_price = min_price - 1
                    condition = 9

                if not rec_price and min_price and our_price < min_price:
                    updated_price = min_price - 1
                    condition = 10

                if min_price == rec_price and rec_price != 0 and (our_price > min_price or our_price < min_price):
                    updated_price = min_price - 1
                    condition = 11

                if our_price == min_price < rec_price:
                    updated_price = min_price
                    condition = 12

                if not rec_price and our_price == min_price:
                    updated_price = min_price
                    condition = 13

                if our_price == rec_price == min_price:
                    updated_price = min_price
                    condition = 14

                if updated_price > abs_min_price:
                    if condition not in [8, 12, 13, 14]:
                        if not debug_mode:
                            url = '%s/api/SetPrice/%s/%s/%s' % (settings.MARKET_DOMAIN, item, updated_price, api_key)
                            data = get_request(url)
                            result = '%s - was=%s, rec=%s, min=%s, set=%s (%s)\n' % \
                                     (name.encode('utf-8'), our_price, rec_price, min_price, updated_price, condition)
                            print data
                            msg.append(result)
                            resp = {'success': True, 'msg': msg}
                    else:
                        result = '%s - was=%s, rec=%s, min=%s, set=%s (%s)\n' % \
                                 (name, our_price, rec_price, min_price, updated_price, condition)
                        msg.append(result)
                        resp = {'success': True, 'msg': msg}

            return HttpResponse(simplejson.dumps(resp), content_type='application/json')

        except UserProfile.DoesNotExist:
            pass
    return render(request, 'update.html', {})


def insert(request):
    try:
        user = UserProfile.objects.get(user=request.user)
        api_key = '?key=%s' % user.api_key
        debug_mode = user.debug_mode
        if request.method == 'POST':
            msg = []
            update_db(db_filename())
            steamcommunity = 'http://steamcommunity.com/profiles/%s/inventory/json/730/2/' % user.steam_username
            response = urllib2.urlopen(steamcommunity)
            inventory = json.load(response)
            for i in inventory['rgInventory'].items():
                for k in i:
                    if isinstance(k, dict):
                        item_id = '%s_%s' % (k['classid'], k['instanceid'])
                        url = '%s/api/ItemInfo/%s/ru/%s' % (settings.MARKET_DOMAIN, item_id, api_key)
                        item = get_request(url)

                        data = process_item(item, api_key, debug_mode)
                        print data
                        msg.append(data)
            resp = {'success': True, 'msg': msg}
            return HttpResponse(simplejson.dumps(resp), content_type='application/json')
        else:
            steamcommunity = 'http://steamcommunity.com/profiles/%s/inventory/json/730/2/' % user.steam_username
            response = urllib2.urlopen(steamcommunity)
            data = json.load(response)
            inv_len = len(data['rgInventory'])
            data = {'inv_len': inv_len}

            return render(request, 'insert.html', data)
    except UserProfile.DoesNotExist:
        pass


def ping(request):
    return render(request, 'ping.html', {})
