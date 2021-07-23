#!/bin/python3
import smtplib
import pyttsx3
################## initialize #####################
sender = 'vo***********or@srmist.edu.in'
receiver = '************@gmail.com'
message = "THIS IS TO INFORM YOU THAT THE LAST COMMAND SENT TO THE VOICROWAVE OVEN IS INVALID, THEREFORE THE COMMAND WILL NOT BE EXECUTED.\nPLEASE TRY AGAIN AFTER FEW MINUTE"
username = "HIDDEN"  
password = "HIDDEN"
engine = pyttsx3.init()       ##Text to Speech Initialized
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
################# execution #####################
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  ##setup SMTP
    server.ehlo()   
    server.starttls()
    server.login(username, password)              ##login using provided credentials
    server.sendmail(sender, receiver, message)    ##sending mail
    server.quit()                                 ##logout and exit after send
    engine.setProperty('voice', voices[2].id)
    engine.say("SOME ERROR HAS OCCURED. AN EMAIL IS SENT REGARDING THIS.")
    engine.runAndWait()
    print ('Email Sent')
except:
    print("Failed To Send Mail")
    print("~Check Internet Connection~")
    engine.setProperty('voice', voices[2].id)
    engine.say("FAILED TO SEND MAIL")
    engine.say("PLEASE CHECK INTERNET CONNECTION")
    engine.runAndWait()
