#!/bin/bash

D=/home/odroid/moussala
L=/data/station
echo Starting AIRDOS data gatherers and upload script
echo -n 'Date: ' 
date

${D}/data-uploader/dataUpload.py ${D}/station/moussala.json >/dev/null 2>${L}/uploader-error.log &

${D}/station/airdos1.py >>${L}/airdos1.log 2>&1 &
${D}/station/airdos2.py >>${L}/airdos2.log 2>&1 &

# This script is started by rc.local
# su odroid -c "bash /home/odroid/moussala/start.sh" >/dev/null 2>>/home/odroid/start-error.log &
