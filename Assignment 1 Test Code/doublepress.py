"""
Author: Julian Chong
Date: 12 Jan 2019
A programs to test whether double presses can be detected.
A double press is when the button is pressed two times within a single second.
"""

import Adafruit_BBIO.GPIO as GPIO
import timeit

GPIO.setup("P8_19", GPIO.IN) 
GPIO.setup("P8_13", GPIO.OUT)

print("Ready")

# function to check if the button has been pressed
def checkButtonPressed():
    if GPIO.input("P8_19") == 1: 
        return True
    return False

numOfPresses = 0
while True:
    if checkButtonPressed():            # once button has been pressed
        while GPIO.input("P8_19") == 1: # wait for the button to be released
            continue
        numOfPresses += 1
        
        # if first time pressing button
        if numOfPresses == 1:       
            start = timeit.default_timer() # start the timer
        # if second time pressing button, and was within the next second of the first press  
        elif numOfPresses == 2 and (timeit.default_timer() - start) <= 1:
            print("Double Press")
            start = timeit.default_timer() # restart the timer
            numOfPresses = 0               # restart numOfPresses counter
            GPIO.output("P8_13", GPIO.HIGH)
        # if second time pressing button, but was not within the next second of the first,  
        elif numOfPresses == 2 and (timeit.default_timer() - start) > 1:
            start = timeit.default_timer() # restart the timer
            numOfPresses = 1               # set numOfPresses back to one

GPIO.cleanup()
