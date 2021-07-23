#!/bin/python3
import RPi.GPIO as GPIO
import pyttsx3
import SEVEN_SEGM
############ setup ##############
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    ##Setup Mode
GPIO.setup(11,GPIO.OUT)     ##Relay Control
GPIO.setup(13,GPIO.IN)      ##Sensor and Door Closed Input 
engine = pyttsx3.init()     ##Text to Speech Initialized
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
############ functions ###############
def Timer(time_in):
    print("Starting Timer...")
    engine.setProperty('voice', voices[2].id)
    engine.say("Starting Timer")
    engine.runAndWait()
    GPIO.output(11,0)
    while(not GPIO.input(13)==1):
        pass
    for i in range(time_in,-1,-1):
        GPIO.output(11,1)
        Display(i)
    print("** ** ** **")
    GPIO.output(11,0)
    engine.setProperty('voice', voices[2].id)
    engine.say("TIMER COMPLETED. END OF TASK.")
    engine.runAndWait()

def Display(count):
    data= int(count)
    minuteH = int((data/60)/10)
    minuteL = int((data/60)%10)
    secondH = int(((data%3600)%60)/10)
    secondL = int(((data%3600)%60)%10)
    print(minuteH,minuteL,"M ",secondH,secondL,"S")
    SEVEN_SEGM.Call(minuteH,minuteL,secondH,secondL)
