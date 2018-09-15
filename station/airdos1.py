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
#from pymlab import config

time.sleep(10)	# delay for initialisation of the RS232/USB convertor

def handle_data(data):
	print data,
	datafname = '/data/station/data/' + str(time.strftime("%Y%m%d%H0000000")) + "_ARA-A3_meta" + ".csv"
	if int(time.strftime('%Y')) >= 2016:
	#if True:
		with open(datafname, "a") as nbf:
			nbf.write(data)
		nbf.close()

# This device tag is bound to serial number of the device
# If you don't know the serial number, replace by /dev/ttyUSB0 or so

# AIRDOS 1
#port = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9GZB15L-if00-port0'
port = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9G7V59L-if00-port0'
#port = '/dev/ttyUSB0'

# AIRDOS 2
#port = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9G7V59L-if00-port0'

baud = 9600

while True:
	try:
		serial_port = serial.Serial(port, baud, timeout=20)

#		cfg = 	config.Config(
#					i2c = {
#						"port": 1,
#					},
#					bus = [
#						{
#						    "name":          "altimet",
#						    "type":        "altimet01",
#						},
#					],
#				)
#
#		cfg.initialize()
#		alt = cfg.get_device("altimet")
#		time.sleep(0.5)

		while True:
			reading = serial_port.readline().rstrip()
			# If we need to parse it
			#values = reading.split(' ')

			# Get temperature and pressure from i2c sensor
#			(t1, p1) = alt.get_tp()
#			t1=0
#			p1=0
			handle_data(str(time.time()) + ',' 
#				+ str(round(t1,2)) + ',' 
#				+ str(round(p1,1)) + ',' 
				+ str(reading) 
				+ str('\n')
				)
			 
	except:
		print "Exception"
		time.sleep(5)
