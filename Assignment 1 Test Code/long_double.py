"""
Author: Julian Chong
Date: 17 Jan 2019
A programs to test whether long presses and double presses can be detected.
Long presses are press that are held longer than 1.5 seconds.
Double presses is a second press that occurred within the next second of the first press.
"""

import Adafruit_BBIO.GPIO as GPIO
import timeit
import time

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
    if checkButtonPressed():                # once button has been pressed
        pressBegin = timeit.default_timer() # start timer to time duration of press
        while GPIO.input("P8_19") == 1:     # wait for the button to be released
            continue
        pressDuration = (timeit.default_timer() - pressBegin)
        
        if pressDuration > 1.5:  # long presses are longer than 2 seconds
            numOfPresses = 0     # reset numofPresses counter
            print("Long Press")
            blinks = 0
            while blinks < 5:    # LED will blink 5 times
                GPIO.output("P8_13", GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output("P8_13", GPIO.LOW) 
                time.sleep(0.3)
                blinks += 1
        
        else:
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
