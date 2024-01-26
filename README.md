# Emergency Response System (Beaglebone Microcontroller IoT Device)

## General Description

FIT3140, a financial institution in Sprintvale, has experienced multiple cases of robbery over the past 5 years, leading to significant financial losses. In response to these challenges, FIT3140 is implementing a dedicated reactive measure to respond to emergencies effectively.

The proposed solution involves discreet buttons within the FIT3140 building, allowing designated personnel to alert the response team during emergencies. These buttons are connected to a Beaglebone microcontroller with internet capabilities, facilitating real-time communication with the response team. Ground staff will be trained to use these buttons, featuring simple click functionality.

The response team can view signals on a private webpage and take immediate actions through a web interface. Quick response times are critical, and actions may include activating the premise alarm or locking safes.

## Project Functional Requirements 


- **LED blinking rapidly:**     
Alarm is being sounded.    

- **LED blinking slowly:**     
Registers have been locked.    

- **LED light up:**     
Safes have been locked.    

- **LED turned off:**     
No current event is occurring.    


## Response Staff

- **To Activate the Alarm:**
    1. Hover over to the "ACTIVATE ALARM DURATION" button and select the desired duration. When the duration is selected, the LED will blink slowly for 10 seconds and then rapidly for the selected duration.

- **To Deactivate the Alarm:**
    1. This can only be done once there is a slow blinking of the LED. Otherwise, wait for slow blinking to occur.
    2. Press "OFF ALARM" once. The LED will now be turned off.

- **To Lock the Safes:**
    1. Press "ON SAFES" once. The LED will now light up.

- **To Unlock the Safes or Disable Alarm:**
    1. If the alarm is being sounded, a slow blinking of the LED will have to occur first.
    2. Press "DISABLE EVENTS" once. The LED will now be turned off. 
    3. Message from Ground Staff at Normal Times: All Good!

- **Ground Staff to Activate Alarm:**
    1. Press the button on the Beagle board once; the LED will blink slowly first and then rapidly until deactivated.
    2. Message from ground staff: Ground staff activated the alarm! HELP!!

- **Ground Staff to Deactivate Alarm:**
    1. Press the button twice on the Beagle board; the LED will now be turned off.
    2. Message from ground staff: Ground staff disabled the alarm!

- **Ground Staff Notify Response Staff to Cancel Event:**
    1. Press the button three times on the Beagle board; the LED will now be turned off.
    2. Message from ground staff: Please cancel all the events


   

## Components
1. **The App:**    
 This would be the Beaglebone Black microcontroller for the ground staff.

2. **The Client:**    
This is the web interface which the response team.

3. **The Server:**     
This will handle the data interchange and sync. For example, it will read data from the app and send it over to the client.

## Installation
1. Connect your BeagleBone Black P8_19 pins
2. Browse to Cloud9 IDE to program your BeagleBone.
3. run the Server.js 
4. browse the web page at: http://192.168.7.2:8888/
5. Refer to https://randomnerdtutorials.com/programming-the-beaglebone-black-with-bonescript/ for more information.