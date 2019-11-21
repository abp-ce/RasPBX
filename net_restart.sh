#!/bin/bash
ping -c4 192.168.0.1 > /dev/null
if [ $? != 0 ] 
then
  sudo ifconfig eth0 down
  sleep 5
  sudo ifconfig eth0 up
fi
