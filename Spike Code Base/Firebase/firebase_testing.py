"""
Author: Julian Chong
Date: 20 Jan 2019
A program that sends and receive data from a Firebase database.
A double press will send a message saying to sound the alarm, and a long press will
send a message to cancel the alarm. Once a signal has been sent, it reads in the message
that the response team sends. The LED will then either turn on or off depending on the message.
"""

from firebase import firebase
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
messageSent = False
while not messageSent:
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
            messageSent = True
            message = 0
        
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
                messageSent = True
                message = 1
            # if second time pressing button, but was not within the next second of the first,  
            elif numOfPresses == 2 and (timeit.default_timer() - start) > 1:
                start = timeit.default_timer() # restart the timer
                numOfPresses = 1               # set numOfPresses back to one

firebase = firebase.FirebaseApplication('https://advanced-programming-11683.firebaseio.com', None)

if message == 1:  # double press = sound the alarm
    msgFromGroundStaff = "ROBBERY, 34th Street 11th Avenue"
    firebase.post('fromGroundStaff', msgFromGroundStaff)
elif message == 0: # long press = cancel the alarm
    msgFromGroundStaff = "FALSE EMERGENCY, CANCEL ALARM"
    firebase.post('fromGroundStaff', msgFromGroundStaff)
    
while True:
    msgFromResponseTeam = firebase.get('', 'fromResponseTeam')

    if msgFromResponseTeam == "Sound Alarm":
        GPIO.output("P8_13", GPIO.HIGH) #Light on
        print("Alarm is being sounded")
    elif msgFromResponseTeam == "Cancel Alarm":
        GPIO.output("P8_13", GPIO.LOW)  #Light off
        print("Alarm has been cancelled")

GPIO.cleanup()
