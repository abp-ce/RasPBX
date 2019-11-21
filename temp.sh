#!/bin/bash
temp="42000"
realtemp=$(</sys/class/thermal/thermal_zone0/temp) 
while [ "$realtemp" -gt "$temp" ]
do
realtemp=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date +"%D %T") ${realtemp:0:2}.${realtemp:2}'C"
sleep 1
done
