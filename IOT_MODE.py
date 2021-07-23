#!/bin/python3
import RPi.GPIO as GPIO
import pyrebase
import TIMER
import DATA_BASE
import pyttsx3
############ setup ##############
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    ##Setup Mode
GPIO.setup(11,GPIO.OUT)     ##relay turned off
engine = pyttsx3.init()     ##Text to Speech Initialized
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
############ configuration ###########
config = {
    "apiKey": "AIzaSyBxPS_eGqlJwyKcBDDF-b2JfTrrFKTiTEc",
    "authDomain": "voicerowave.fire****app.com",
    "databaseURL": "https://voicerowave.fire****io.com",
    "projectId": "voicerowave",
    "storageBucket": "voicerowave.********.com",
    "messagingSenderId": "771062305817"
  }
############ initialize #################
GPIO.output(11,0)
firebase = pyrebase.initialize_app(config)
db = firebase.database()                ##Firebase Initialization
engine.setProperty('voice', voices[2].id)
engine.say("TURN ON YOUR ANDROID APPLICATION TO CONTROL")
engine.runAndWait()
db.child("ANDROID/VOICE").set(0)
db.child("ANDROID/BUTTON").set(0)

################# execution ##################
while True:
    data = db.child("ANDROID/VOICE").get().val()
    dat = db.child("ANDROID/BUTTON").get().val()
    data1=int(dat)
    if((data == 0 or data == "\"\"") and (data1 == 0)):
        pass
    else:
        try:
            if(not data == 0 and not data == "\"\"" and not data == "0"):
                print(data)
                data_arr = data.split()
                item = data_arr[0]
                unit = data_arr[2]
                if (data_arr[1] == 'one'):
                    quan = 1
                if (data_arr[1] == 'two'):
                    quan = 2
                if (data_arr[1] == 'three'):
                    quan = 3
                if (data_arr[1] == 'four'):
                    quan = 4
                if (data_arr[1] == 'five'):
                    quan = 5
                if (data_arr[1] == 'six'):
                    quan = 6
                if (data_arr[1] == 'seven'):
                    quan = 7
                if (data_arr[1] == 'eight'):
                    quan = 8
                if (data_arr[1] == 'nine'):
                    quan = 9
                if (data_arr[1] == 'ten'):
                    quan = 10
                else:
                    quan = data_arr[1]
                DATA_BASE.MAIN(item,quan,unit)
                db.child("ANDROID/VOICE").set(0)
            elif(not data1 == 0):
                print(data1)
                TIMER.Timer(data1)
                db.child("ANDROID/BUTTON").set(0)
        except:
            db.child("ANDROID/VOICE").set(0)
            db.child("ANDROID/BUTTON").set(0)
            import ERR_MAIL
            pass
