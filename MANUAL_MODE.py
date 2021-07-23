#!/bin/python3
import RPi.GPIO as GPIO
import pyttsx3
import TIMER
######## setup #########
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)      ##Setup Mode
GPIO.setup(11,GPIO.OUT)       ##Relay Control
engine = pyttsx3.init()       ##Text to Speech Initialized
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
################## initialize #####################
GPIO.output(11,0)
temp = int(0)
engine.setProperty('voice', voices[2].id)
engine.say("USE KEYPAD TO CONTROL")
engine.runAndWait()
################## functions #####################
class keypad():
    def __init__(self, columnCount = 3):
        if columnCount is 3:
            self.KEYPAD = [
                [1800,60,5],
                [3600,300,10],
                [5400,600,30],
                ["START",0,"MAIL"]
            ]

            self.ROW         = [37,35,33,31]
            self.COLUMN      = [29,23,21]
        else:
            return
     
    def getKey(self):
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
        if rowVal <0 or rowVal >3:
            self.exit()
            return
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
        if colVal <0 or colVal >2:
            self.exit()
            return
        self.exit()
        return self.KEYPAD[rowVal][colVal]
    
    def exit(self):
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
################# execution #####################
kp = keypad()
while True:
    if(temp > 5940):
        engine.setProperty('voice', voices[2].id)
        engine.say("TIMER EXCEEDED")
        engine.runAndWait()
        print("TIMER EXCEEDED")
        temp = 0
        engine.setProperty('voice', voices[2].id)
        engine.say("TIMER IS NOW CLEARED")
        engine.say("PROVIDE ANOTHER INPUT")
        engine.runAndWait()
        print("TIMER IS CLEARED")
    else:
        digit = kp.getKey()
        TIMER.Display(temp)
        if not digit ==None:
            while not kp.getKey()==None:
                pass
            if(digit == 'MAIL'):
                engine.setProperty('voice', voices[2].id)
                engine.say("YOU HAVE PRESSED THE SERVICE BUTTON")
                engine.say("THIS IS TO INFORM YOU THAT OVEN WILL NOT WORK NOW AND AN EMAIL HAS BEEN SENT TO THE TECHNICIAN")
                engine.say("IF IT IS DONE BY MISTAKE KINDLY RESTART THE OVEN")
                engine.say("IT IS RECOMMENDED NOT TO USE THE OVEN TILL THE PROBLEM IS SOLVED")
                engine.say("INCASE OF URGENCY YOU CAN CALL TO THE TECHNICIAN. KINDLY NOTE THE NUMBER")
                engine.say("9*********4")
                engine.runAndWait()
                import SERVICE_MAIL
                while True:
                    pass
            if(digit == 0):
                temp = 0
                TIMER.Display(0)
            if(digit == 'START'):
                TIMER.Timer(temp)
                temp = 0
            else:
                temp = temp + int(digit)            
                TIMER.Display(temp)
                print(temp)
