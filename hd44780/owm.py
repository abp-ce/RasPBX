#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Roman Vishnevsky aka.x0x01 @ gmail.com

import urllib2
import json
#import hashlib
#import uuid
#import os
#import lcddriver
#from datetime import datetime

# обработчик исключений
try:
    # запрос
    request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?id=515879&units=metric&lang=ru&APPID=a1eaeeb1587b0f8f19fa1f8e33d404be')
    response = urllib2.urlopen(request)
    # работа с JSON
    result = json.loads(response.read())

    fl = open('owm.dat', 'w+')
    #lcd = lcddriver.lcd()
    #lcd.lcd_clear()
    #now = datetime.now()
    #str = now.strftime("%d %b %a  %H:%M")
    #lcd.lcd_display_string(str, 1)
    str = "%.1f" % float(repr(result['main']['temp'])) + "'C " + "%.0f" % float(repr(result['main']['pressure'])) + "hPa " + repr(result['main']['humidity']) + "%"
    fl.write(str)
    fl.write('\n')
    #lcd.lcd_display_string(str, 2)
    str = "%.1f" % float(repr(result['wind']['speed'])) + "m/s  " + "%.1f" % float(repr(result['wind']['deg'])) + "'"
    fl.write(str)
    #lcd.lcd_display_string(str, 3)
    #str=os.popen('uptime').read()
    #lcd.lcd_display_string(str[10:27], 4)

except urllib2.URLError, e:
    print 'HTTP error:', e

except (ValueError, TypeError), e:
    print 'JSON error:', e

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

finally:
    fl.close()
