# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print " mode ="+str(mode)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=5
StepPinBackward=3
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)

def forward(x):
    GPIO.output(StepPinForward, GPIO.HIGH)
    print "forwarding running  motor "
    time.sleep(x)
    GPIO.output(StepPinForward, GPIO.LOW)

def reverse(x):
    GPIO.output(StepPinBackward, GPIO.HIGH)
    print "backwarding running motor"
    time.sleep(x)
    GPIO.output(StepPinBackward, GPIO.LOW)

while 1:
   
   inkey = raw_input()
   if inkey == "8":
      forward(1)
   elif inkey == "2":
      reverse(1)
   else:
      print "Other input"


print "Stopping motor"
GPIO.cleanup()
