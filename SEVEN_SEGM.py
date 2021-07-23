#!/bin/python3
import RPi.GPIO as GPIO
import time
############ setup ##############
GPIO.setmode(GPIO.BOARD)    ##Setup Mode
GPIO.setwarnings(False)
############ initialize #################
zero = [18,22,24,26,32,36]
one = [22,24]
two =[18,22,26,32,38]
three = [18,22,24,26,38]
four = [22,24,36,38]
five = [18,24,26,36,38]
six = [18,24,26,32,36,38]
seven = [18,22,24]
eight = [18,22,24,26,32,36,38]
nine = [18,22,24,26,36,38]
all_led = [8,10,12,16,18,22,24,26,32,36,38]
segment =  [18,22,24,26,32,36,38]
ls=[8,10,16,12]
############ functions #################
def num(val):
    if val == 0:
        for i in segment:
            GPIO.output(i,1)
        for i in zero:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 1:
        for i in segment:
            GPIO.output(i,1) 
        for i in one:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 2:
        for i in segment:
            GPIO.output(i,1)
        for i in two:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 3:
        for i in segment:
            GPIO.output(i,1)
        for i in three:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 4:
        for i in segment:
            GPIO.output(i,1)
        for i in four:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 5:
        for i in segment:
            GPIO.output(i,1)
        for i in five:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 6:
        for i in segment:
            GPIO.output(i,1)
        for i in six:
            GPIO.output(i,0)
            time.sleep(0.001)
    if val == 7:
        for i in segment:
            GPIO.output(i,1)
        for i in seven:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 8:
        for i in segment:
            GPIO.output(i,1)
        for i in eight:
            GPIO.output(i,0)
            time.sleep(0.0001)
    if val == 9:
        for i in segment:
            GPIO.output(i,1)
        for i in nine:
            GPIO.output(i,0)
            time.sleep(0.0001)
            
def Call(w,x,y,z): 
    for s in all_led:
        GPIO.setup(s,GPIO.OUT)
        GPIO.output(s,1)
    for s in ls:
        GPIO.output(s,0)
    
    for i in range (20):
        for s in ls:
            for f in ls:
                GPIO.output(f,0)
            GPIO.output(s,1)
            if(s == 8):
                num(w)
            if(s == 10):
                num(x)
            if(s == 16):
                num(y)
            if(s == 12):
                num(z)
            time.sleep(0.01)
    for i in segment:
        GPIO.output(i,1)
