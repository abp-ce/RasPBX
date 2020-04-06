#!/bin/bash
#mkfs.ext4 /dev/mmcblk0p3
mount /dev/mmcblk0p3 /mnt/backup/
rsync -aAXv --delete --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /mnt/backup/
mount /dev/mmcblk0p2 /mnt/archave/
rm /mnt/archave/*.tar.gz
tar -czf /mnt/archave/raspbx-$(date +%F).tar.gz -C /mnt/backup/ ./
umount /mnt/backup/
s3cmd put /mnt/archave/ras*.tar.gz s3://abp-rasp
umount /mnt/archave/
#s3cmd --dry-run --delete-removed --exclude-from=exclude-backup sync / s3://raspbx


