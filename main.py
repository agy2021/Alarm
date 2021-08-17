import datetime
from playsound import playsound
import webbrowser
import time

x = datetime.datetime.now()
y = x.strftime("%I:%M:%S")

print("Time when program started: ", y)

hour = input("What hour do you want the alarm to go off? ")
minute = input("What minute do you want the alarm to go off? ")
second = input("What second do you want the alarm to go off (type '00' if you want the program to go off at a certain minute)? ")

usertime = input("Would you like to keep showing the current time? (y/n). ")

print("Alarm has been set.")

while (True):
    a = datetime.datetime.now()
    b = a.strftime("%I:%M:%S")

    if "y" in usertime:
        print(b)
        time.sleep(1)

    if a.strftime("%I") == hour and a.strftime("%M") == minute and a.strftime("%S") == second:
        print("\nYour alarm will go off now.")
        print("Press the keys 'Ctrl' + 'C' to terminate program.")

        playsound("start.wav")
        webbrowser.open("music.mp3")