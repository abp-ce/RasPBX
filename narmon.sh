#!/bin/bash
req=$(curl -s 'http://narodmon.ru/api/sensorsOnDevice?id=1222&uuid=b7ded2ab8ea69e6b2ed8ec240c93ec47&api_key=pZ6sg0Ew6rxkD&lang=en' -H 'User-Agent: RaspberryPiApp')
temp=$(echo ${req} | jq '.sensors[0].value')
echo "Температура $temp С"
hum=$(echo ${req} | jq '.sensors[1].value')
echo "Влажность $hum %"
pres=$(echo ${req} | jq '.sensors[2].value')
echo "Давление $pres мм.рт.ст"
