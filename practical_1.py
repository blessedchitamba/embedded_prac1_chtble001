#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

#global count variable
global counter
counter = 0

led_outputs = list(product([0,1], repeat=3))

#function to increment or decrement the counter var depending on the button pressed
def update_count(num):
    global counter
    counter = (counter+num)%8
    print(counter)
    
#callback functions for push buttons
#the one to add one to the counter
def add_event(channel):
    print("event detected!")
    print(channel)
    
    if channel==13:
    	update_count(1)
    elif channel==15:
    	update_count(-1)
    	
    showLEDs()

#function to show the leds after button is pressed
def showLEDs():
    GPIO.output(7, led_outputs[counter][2])
    GPIO.output(11, led_outputs[counter][1])
    GPIO.output(12, led_outputs[counter][0])
    print("done showing leds")

#function to set up the  inputs and all
def initialize():
    #set the mode of the numbering of the pins
    GPIO.setmode(GPIO.BOARD)

    #create lists of the input and output number channels
    output_list = [7, 11, 12]
    input_list = [13, 15]

   #set up the channels and add event detects to input channels 
    GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(13, GPIO.RISING, callback=add_event, bouncetime=500)
    GPIO.add_event_detect(15, GPIO.RISING, callback=add_event, bouncetime=500)

    print("done initializing")
   
    """
    while True:
    	GPIO.output(output_list, GPIO.HIGH)
    	sleep(1)
    	GPIO.output(output_list, GPIO.LOW)
    	sleep(1)
    """

#main function just sleeps
def main():
    sleep(0.1)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
    	initialize()
    	showLEDs()
    	print("Press button to start counter...")
        while True:
             main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
