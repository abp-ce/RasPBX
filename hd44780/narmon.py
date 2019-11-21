#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Roman Vishnevsky aka.x0x01 @ gmail.com

import urllib2
import json
import hashlib
import uuid
import lcddriver
from datetime import datetime

# ключ API для разработчика, получаемый в Мои данные \ Мои ключи API после регистрации в проекте.
# заменить на свой!
api_key = 'qP61RWrR78gHT'

# генерация уникального ID приложения
app_id = str(uuid.getnode())
md5_app_id = hashlib.md5(app_id).hexdigest()

# формирование тела JSON
data = {
    'cmd': 'sensorsOnDevice',
    'id': 1222,
    'uuid': md5_app_id,
    'api_key': api_key,
    'lang': 'en'
}

# обработчик исключений
try:
    # запрос
    request = urllib2.Request('http://narodmon.ru/api', json.dumps(data))
    response = urllib2.urlopen(request)
    # работа с JSON
    result = json.loads(response.read())

    # вывод всего массива
    #print json.dumps(result, indent=4, sort_keys=True)
    # или по ключу
    # print result['devices']
    # или по ключу в цикле
    # for dev in result['devices']:
    #     print dev['name'], dev['distance']
    #print "Температура ", result['sensors'][0]['value'], "C"
    #print "Влажность ", result['sensors'][1]['value'], "%"
    #print "Давление ", result['sensors'][2]['value'], "мм.рт.ст."
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
    now = datetime.now()
    str = now.strftime("%d %b %a  ") + repr(result['sensors'][0]['value']) + "%"
    #print str
    lcd.lcd_display_string(str, 1)
    str = repr(result['sensors'][1]['value']) + "C  " + repr(result['sensors'][1]['value']) + "mm"
    #print str
    lcd.lcd_display_string(str, 2)

except urllib2.URLError, e:
    print 'HTTP error:', e

except (ValueError, TypeError), e:
    print 'JSON error:', e

