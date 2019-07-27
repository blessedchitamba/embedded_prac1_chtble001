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

# Logic that you write
def main():
    #set the mode of the numbering of the pins
    GPIO.setmode(GPIO.BOARD)

    #create lists of the input and output number channels
    output_list = [7, 11, 12]
    input_list = [13, 15]

    
    GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
   # print("write your logic here")

    while True:
    	GPIO.output(output_list, GPIO.HIGH)
    	sleep(1)
    	GPIO.output(output_list, GPIO.LOW)
    	sleep(1)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
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
