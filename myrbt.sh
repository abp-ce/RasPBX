#!/bin/sh
/boot/grep /dev/root /proc/mounts > /dev/null 2>&1
if [ $? -ne 0 ]
then
 /boot/echo b > /proc/sysrq-trigger
fi

