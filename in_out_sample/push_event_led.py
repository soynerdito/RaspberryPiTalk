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
    GPIO.wait_for_edge(2, GPIO.FALLING)
    led_on = not led_on
    GPIO.output( 11, led_on )

#Turn it off to leave it off
GPIO.output( 11, False )
GPIO.cleanup()
