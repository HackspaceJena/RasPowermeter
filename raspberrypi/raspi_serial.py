#!/usr/bin/python3

import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

# read Arduino

while True:

    input = ser.readline()

    input_number = input

    print ("Time: " + str(int(time.time())) + " Reflection Value: " + str(input_number)[:-2] + "[v]")
