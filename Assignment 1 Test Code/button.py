"""
Author: Teh Run Xun
Date: 12 Jan 2019
A simple python program where the led light will keep on blinking when the button is pressed.
"""

import Adafruit_BBIO.GPIO as GPIO

#The pin key for input which is the button is at P8_19
GPIO.setup("P8_19", GPIO.IN)
#The pin key for output which is the led light is at P8_13
GPIO.setup("P8_13", GPIO.OUT)

while True:
  if GPIO.input("P8_19") == 1:  #When the button is pressed, led light blink
    while True:
      GPIO.output("P8_13", GPIO.HIGH) #Light on
      time.sleep(0.3)
      GPIO.output("P8_13", GPIO.LOW)  #Light off
      time.sleep(0.3)
"""
Clean up all the ports that have been used.
This prevents damage, e.g. a port set to HIGH as output but accidentally connect it to LOW
which would short-circuit the port and possibly fry it.
"""
GPIO.cleanup()
