#!/bin/bash

D=/home/odroid/station
L=/data/station
echo Starting AIRDOS data gatherers and upload script
echo -n 'Date: ' 
date

${D}/data-uploader/dataUpload.py ${D}/station/aragats.json >/data/log/uploader.log 2>${L}/uploader-error.log &

${D}/station/airdos1.py >>${L}/airdos1.log 2>&1 &
#${D}/station/airdos2.py >>${L}/airdos2.log 2>&1 &

# This script is started by rc.local
#while [ ! /usr/bin/ntpstat ] ; do echo Waiting for NTP service to settle. >>/home/odroid/start.log ; sleep 5 ; done
#sleep 10
#su odroid -c "bash /home/odroid/station/start.sh" >>/home/odroid/start.log 2>>/home/odroid/start-error.log &

