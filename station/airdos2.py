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

time.sleep(10)	# delay for initialisation of the RS232/USB convertor

def handle_data(data):
	print data,
	datafname = '/home/odroid/station/data/' + str(time.strftime("%Y%m%d%H0000000")) + "_MUS-A2_meta" + ".csv"
	if int(time.strftime('%Y')) >= 2016:
	#if True:
		with open(datafname, "a") as nbf:
			nbf.write(data)
		nbf.close()

# This device tag is bound to serial number of the device
# If you don't know the serial number, replace by /dev/ttyUSB0 or so

# AIRDOS 1
#port = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9GZB15L-if00-port0'

# AIRDOS 2
port = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9G7V59L-if00-port0'

baud = 9600

while True:
		serial_port = serial.Serial(port, baud, timeout=20)
		while True:
			reading = serial_port.readline().rstrip()
			# If we need to parse it
			#values = reading.split(' ')

			handle_data(str(time.time()) + ',' 
				+ str(reading) 
				+ str('\n')
				)
