#!/usr/bin/python3

from datetime import datetime
from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

clkPin = 24
GPIO.setup(clkPin,GPIO.OUT)

oldsec = datetime.now().second

print("Starting clock pulse out")

while(1):

    while (oldsec == datetime.now().second):
        sleep(0.1)

    GPIO.output(clkPin,1)
    sleep(0.1)
    GPIO.output(clkPin,0)
#    print(".")
    oldsec = datetime.now().second

