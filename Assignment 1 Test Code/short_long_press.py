"""
Author: Julian Chong
Date: 12 Jan 2019
A programs to test whether short presses and long presses can be detected.
Short presses will cause the LED to blink exactly 5 times.
Long presses will cause the LED to light up.
"""

import Adafruit_BBIO.GPIO as GPIO
import timeit
import time
 
GPIO.setup("P8_19", GPIO.IN) 
GPIO.setup("P8_13", GPIO.OUT)

print("Ready")
 
while True:
    if GPIO.input("P8_19") == 1:
        taken = 0
        start = timeit.default_timer()
        while GPIO.input("P8_19") == 1:
            taken = (timeit.default_timer() - start) # duration of button being held
            
        if taken >= 0.5 and taken <= 2: # short presses are held longer than 0.5 seconds and shorter than 2 seconds
            print("Short press")    
            blinks = 0
            while blinks < 5:       # LED will bink 5 times
                GPIO.output("P8_13", GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output("P8_13", GPIO.LOW) 
                time.sleep(0.3)
                blinks += 1
        elif taken > 2:                 # long presses are held longer than 2 seconds
            GPIO.output("P8_13", GPIO.HIGH)
            print("Long press")
            
GPIO.cleanup()
