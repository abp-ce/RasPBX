echo $(date)
/usr/sbin/asterisk -rx 'dongle cmd dongle0 AT+CPMS=\"SM\",\"SM\",\"SM\"'
/usr/sbin/asterisk -rx 'dongle cmd dongle0 AT+CMGD=1,4'
/usr/sbin/asterisk -rx 'dongle cmd dongle0 AT+CPMS=\"ME\",\"ME\",\"ME\"'
/usr/sbin/asterisk -rx 'dongle cmd dongle0 AT+CMGD=1,4'
