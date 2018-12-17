# DESK AUTOMATION
### This is a Proof-of-Concept for the company 'Illumination Works', where the goal is to automate desk actions to demonstrate accurate phrase/voice recognition capabilities. Here are a list of some of the commands that it can recognize and the actions they take:

## PREREQS:
- A raspberry pi
- The Matrix Creator (A sensor board)
- Matrix Creator dependencies and python 3.6+
OPTIONAL:
- USB Fan
- Bluetooth Speaker /w known MAC address

## INSTRUCTIONS: 

1. Troubleshoot and fix all errors that occur while trying to run the script 'illuminate.py' (Dependencies, local variables, etc)

2. Once all common errors and problems are solved, run the script by typing 'python illuminate.py'

2b. Optional: Edit connect_bluetooth.sh to have a MAC address that reflects your bluetooth device.

3. Script is now running! Make vocal commands as shown below:







### 'Illuminate' 
= Saying this word/command turns on the lights on my desk, including christmas lights. It does this using python modules, regular expressions, and a tp-link API that talks to a smart wi-fi plug.



### 'LED Show'
= Saying this command activates a mini light show using the array of LED's onboard. This is done with a script given by the creators of the Matrix Creator, which is found at the repo here: https://github.com/matrix-io/matrix-creator-hal/tree/master/demos - Script called 'everloop_demo.cpp' [C++]



### 'Compass'
= Saying this command utilizes the LED's on the matrix creator to create a compass.



### 'Desk Power'
= Saying this command toggles power to my workstation and everything on it, including the monitors and accessories. This is to help conserve energy, and can also be set to turn off/on based on a timer. This also uses smart wi-fi plug technology. (https://github.com/softScheck/tplink-smartplug)



### 'Tequila'
= Saying this command activates the 'easter egg', which is playing the song 'Tequila' by The Champs through a bluetooth speaker with a specific MAC address, using omxplayer.



### 'Fan my fingers'
=Saying this command toggles a desk fan by turning on and off a usb port on the raspberry pi ;)






LOTS of love and appreciation for the creator of Snowboy, what a god. Please check out his API and send him a thanks! :)
https://snowboy.kitt.ai/
http://docs.kitt.ai/snowboy/
https://github.com/kitt-ai/snowboy

Also other resources that were used/useful:
https://github.com/matrix-io
https://github.com/softScheck/tplink-smartplug

-Lane
