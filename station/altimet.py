#!/usr/bin/python
#
# Serial line logger
# Adapted from: Mrakomer poller at Lomnicky stit, 171209
# 

import time
import datetime
import logging
import serial
import math
from pymlab import config

time.sleep(10)	# delay for initialisation of the RS232/USB convertor

def handle_data(data):
	print data,
	datafname = '/home/odroid/data/' + str(time.strftime("%Y%m%d%H0000000")) + "_MUS-altimet_meta" + ".csv"
	if int(time.strftime('%Y')) >= 2016:
	#if True:
		with open(datafname, "a") as nbf:
			nbf.write(data)
		nbf.close()

while True:
	try:
		serial_port = serial.Serial(port, baud, timeout=20)

		cfg = 	config.Config(
					i2c = {
						"port": 1,
					},
					bus = [
						{
						    "name":          "altimet",
						    "type":        "altimet01",
						},
					],
				)

		cfg.initialize()
		alt = cfg.get_device("altimet")
		time.sleep(0.5)

		while True:
			# Get temperature and pressure from i2c sensor
			(t1, p1) = alt.get_tp()
			handle_data(str(time.time()) + ',' 
				+ str(round(t1,2)) + ',' 
				+ str(round(p1,1)) + ',' 
				+ str('\n')
				)
			 
	except:
		print "Exception"
		time.sleep(5)
