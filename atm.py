# Design a simple bank system
# Which asks for input like following
#1.withdrawal
#2.balance
#3.break
#use pyttsx3 to provide text to speech

import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume',1)

def bank():
    print("Pick your choice.")
    engine.say("Pick your choice")
    engine.runAndWait()
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Break")


ban1k()
choice = int(input())

while(True):
    if(choice == 1):
        print("Withdrawl successfull.")
        engine.say("Withdrawl successfull.")
        engine.runAndWait()
        bank()
        choice = int(input())
    elif(choice == 2):
        print("You are Bankrupt")
        engine.say("You are Bankrupt")
        engine.runAndWait()
        bank()
        choice = int(input())
    elif(choice == 3):
        print("Checkout successfull. Thank you.")
        engine.say("Checkout successfull. Thank you.")
        engine.runAndWait()
        break
    else:
        print("Invalid input.")
        print("Please try again.")
        engine.say("Invalid input. Please try again.")
        engine.runAndWait()
        bank()
        choice = int(input())

