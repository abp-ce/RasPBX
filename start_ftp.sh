#!/bin/bash
service vsftpd start
mount -t ntfs-3g /dev/sda1 /mnt/ntfs -o rw,uid=ftp_user,gid=ftp
mount --bind /mnt/ntfs /home/ftp_user
