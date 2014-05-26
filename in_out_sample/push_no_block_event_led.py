#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
from remotealert import RemoteAlert

GPIO.setmode(GPIO.BCM)
GPIO.setup( 2, GPIO.IN)
GPIO.setup( 3, GPIO.IN)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW )

led_on = False
ra = RemoteAlert()
dev_id = 'a32b831c-7623-4c43-99cf-b614ff54e902'

def postAndroid(channel):
    ra.send( dev_id, 'Message from pi' )
    print 'Push called'
#GPIO.RISING
GPIO.add_event_detect(3, GPIO.FALLING, callback=postAndroid, bouncetime=300)

while True:
    #GPIO.input( 2 ) == False when pressed
    GPIO.wait_for_edge(2, GPIO.FALLING)
    led_on = not led_on
    GPIO.output( 11, led_on )

#Turn it off to leave it off
GPIO.output( 11, False )
GPIO.cleanup()

