#!/bin/python3
import smtplib
import pyttsx3
################## initialize #####################
sender = 'voicerowave.major@gmail.com'
receiver1 = 'kitrakatpug21@gmail.com'
receiver2 = 'manasvibhargava18@gmail.com'
message = "THIS IS TO INFORM THAT THE SERVICE BUTTON HAD BEEN PRESSED IN THE VOICEROWAVE OVEN. KINDLY CONTACT THE CUSTOMER"
username = 'voicerowave.major@gmail.com'  
password = 'VOICEROWAVE123'
engine = pyttsx3.init()       ##Text to Speech Initialized
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
################# execution #####################
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)   ##setup SMTP
    server.ehlo()
    server.starttls()
    server.login(username, password)               ##login using provided credentials
    server.sendmail(sender, receiver1, message)    ##sending mail receiver1
    server.sendmail(sender, receiver2, message)    ##sending mail receiver2
    server.quit()
    engine.setProperty('voice', voices.id)
    engine.say("AN EMAIL IS SENT SUCCESSSFULLY REGARDING THE SERVICE REQUEST")
    engine.say("WAIT FOR A RESPONSE OR CALL ON THE PROVIDED CONTACT NUMBERS")
    engine.runAndWait()
    print ('Email Sent')
except :
    print("Failed To Send Mail")
    print("~Check Internet Connection~")
    engine.setProperty('voice', voices.id)
    engine.say("FAILED TO SEND MAIL")
    engine.say(" PLEASE CHECK INTERNET CONNECTION")
    engine.runAndWait()
