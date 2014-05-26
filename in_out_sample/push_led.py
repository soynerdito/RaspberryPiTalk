#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup( 2, GPIO.IN)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW )

led_on = False

while True:
    #GPIO.input( 2 ) == False when pressed
    GPIO.output( 11, not GPIO.input( 2 ) )
    sleep(0.1);
