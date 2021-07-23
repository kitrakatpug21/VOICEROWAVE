#!/bin/python3
import RPi.GPIO as G
import pyttsx3
######## setup #########
G.setwarnings(False)
G.setmode(G.BOARD)      ##Setup Mode
G.setup(11,G.OUT)       ##Relay Control
G.setup(15,G.IN)        ##IOT Mode
G.setup(19,G.IN)        ##Manual Mode
################## initialize #####################
G.output(11,0)          ##relay turned off
engine = pyttsx3.init() ##Text to Speech Initialized
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("Welcome to Voicerowave Oven..")
engine.runAndWait()
################# execution #####################
while True:
    ################ IOT #####################
    if(G.input(15) == 1):
        while(G.input(15) == 1):
            pass
        if(G.input(15) == 0):
            print("IOT MODE")
            engine.setProperty('voice', voices[2].id)
            engine.say("I.O.T. MODE Turned On")
            engine.runAndWait()
            import IOT_MODE
    ################ MANUAL ##################
    if(G.input(19) == 1):
        while(G.input(19) == 1):
            pass
        if(G.input(19) == 0):
            print("MANUAL MODE")
            engine.setProperty('voice', voices[2].id)
            engine.say("MANUAL MODE Turned On")
            engine.runAndWait()
            import MANUAL_MODE
    else:
        pass
