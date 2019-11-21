#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Roman Vishnevsky aka.x0x01 @ gmail.com

import urllib2
import json

# формирование тела JSON
data = {"lat":"54.487870","lon":"53.475934"}

hdrs = {
    'X-Yandex-API-Key': "fa732e9f-07d4-475d-a5a9-f4a563bb7709"
    }

# обработчик исключений
try:
    # запрос
    request = urllib2.Request('https://api.weather.yandex.ru/v1/informers?lat=54.487870&lon=53.475934', headers = hdrs)
    response = urllib2.urlopen(request)
    # работа с JSON
    result = json.loads(response.read())

    fl = open('yandex.dat', 'w+')

    str = repr(result['fact']['temp']) + "'C " + repr(result['fact']['pressure_mm']) + "mm " + repr(result['fact']['humidity']) + "%"
    fl.write(str)
    fl.write('\n')
    str = repr(result['fact']['wind_speed']) + "m/s " + repr(result['fact']['wind_dir'])[2:-1]
    fl.write(str)

except urllib2.URLError, e:
    print 'HTTP error:', e

except (ValueError, TypeError), e:
    print 'JSON error:', e

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

finally:
    fl.close()

