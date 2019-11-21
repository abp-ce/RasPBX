#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Roman Vishnevsky aka.x0x01 @ gmail.com

#import urllib2
#import json
#import hashlib
#import uuid
import os
import Adafruit_DHT
import lcddriver
from datetime import datetime

lcd = lcddriver.lcd()

# обработчик исключений
try:
    # запрос
    #request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?id=515879&units=metric&lang=ru&APPID=a1eaeeb1587b0f8f19fa1f8e33d404be')
    #response = urllib2.urlopen(request)
    # работа с JSON
    #result = json.loads(response.read())
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 23)
    fl = open('yandex.dat', 'r+')
    #lcd = lcddriver.lcd()
    lcd.lcd_clear()
    now = datetime.now()
    str = now.strftime("%d %b %a  %H:%M")
    lcd.lcd_display_string(str, 1)
    #str = "%.1f" % float(repr(result['main']['temp'])) + "'C " + "%.1d" % float(repr(result['main']['pressure'])) + "hPa " + repr(result['main']['humidity']) + "%"
    str=fl.readline()
    #fl.write('\n')
    lcd.lcd_display_string(str[:-1], 2)
    #str = repr(result['wind']['speed']) + "m/s  " + repr(result['wind']['deg']) + "'"
    str=fl.readline() + "   {0:0.1f}'C".format(temperature)
    #fl.write(str)
    lcd.lcd_display_string(str, 3)
    str="Uptime " + os.popen("awk '{print int($1/86400)\" days \"int($1%86400/3600)\":\"int(($1%3600)/60)}' /proc/uptime").read()
    lcd.lcd_display_string(str[:-1], 4)
    #[str.find("up"):str.find(':',8)+3], 4)

#except urllib2.URLError, e:
#    print 'HTTP error:', e

#except (ValueError, TypeError), e:
#    print 'JSON error:', e

except IOError as e:
   lcd.lcd_display_string("I/O error({0}): {1}".format(e.errno, e.strerror))

finally:
    fl.close()
