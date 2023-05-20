import os
import time as t
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime as dt
import pyautogui as p
import tkinter as tk

timeNow=dt.datetime.now()
non=1
yNn=0
finalHour=0
finalMinute=0
finalSec=0
exitkey=["quit","stop","bye","exit","kill","die"]
desc=["who are you","what can you do","what are your","who is this","introduce yourself","how can you help me","identify yourself"]

def intro():
    speak("Hello! I'm a Basic Helpful Assistant Incorporation, abbreviated as B H A I but you can call me bhai. would you like to know about my features?")
    reply=user_audio()
    if "y" or "sure" in reply:
        speak("I'm a prototype developed for the purpose of helping you in your day to day activities. Here is a description box stating my features!")
    else:
        pass
def speak(text):
    tts=gTTS(text=text,lang="en")
    filename=r"demo.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def user_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        user=""
        try:
            user=r.recognize_google(audio)
            if user=="":
                pass
            else:
                print(user)
        except Exception as e:
            print()
    return(user)
def timer():
    counter = 0
    def counter_label(label):
      counter = 0
      def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
      count()

    root = tk.Tk()
    root.title("Counting Seconds")
    label = tk.Label(root,fg="dark green")
    label.pack()
    counter_label(label)
    button = tk.Button(root,activebackground="dark green",activeforeground="red", text='Stop', width=25, command=root.destroy)
    button.pack()
    root.mainloop()

def alarmPrompt():
    global finalTime
    global alarmType
    global non
    global amOrpm
    global yNn
    flag=1
    alarmType=p.confirm("Enter which format you prefer","ALARM",["AM/PM","military format"])
    while flag==1:
        finalTime=p.prompt("Enter time in a (Hour:minute) format","ALARM")
        if finalTime==None:
            break
        split = finalTime.split(":")
        try:
            finalHour=int(split[0])
            finalMinute=int(split[1])
            if len(split)==3:
                takeOut=p.confirm("You have entered seconds too?","ALARM",["Use them","Do not use"])
                if takeOut=="Use them":
                    finalSec=int(split[2])
                    yNn=1
            if alarmType == "AM/PM":
                if finalHour<=12 and finalMinute<60 :
                    if yNn == 1:
                        if finalSec<60:
                            amOrpm=p.confirm("Enter The Respective Time Frame","ALARM",["AM","PM"])
                            if amOrpm=="PM":
                                if finalHour>0 and finalHour<12:
                                    finalHour=finalHour+12
                                elif finalHour == 12:
                                    finalHour = 12
                                else:
                                    p.alert("Entered Time was faulty","ALARM")
                        else:
                            if finalHour==12:
                                finalHour=0
                    else:
                         amOrpm=p.confirm("Enter The Respective Time Frame","ALARM",["AM","PM"])
                         if amOrpm=="PM":
                             finalHour=finalHour+12
                         else:
                             if finalHour==12:
                                finalHour=0
                else:
                    flag=flag+1
                    p.alert("ENTERED NUMBERS EXCEED TIME FRAME. PLEASE ENTER AGAIN.","ALARM")
            elif alarmType == "military format":
                if finalHour>23 or finalMinute>59:
                    flag=flag+1
                    p.alert("ENTERED NUMBERS EXCEED TIME FRAME. PLEASE ENTER AGAIN.","ALARM")
            flag=flag-1
            print(finalHour,finalMinute)
        except :
            if non == 1:
                ret=p.confirm("ENTERED DATA NOT IN MENTIONED FORMAT","ALARM",["Re-enter"])
            if ret=="Re-enter":
                continue
            else:
                break
            print(non)
    while (1==1):
        if(finalHour==dt.datetime.now().hour and finalMinute==dt.datetime.now().minute):
           speak("Time's Up!")
           p.alert("Time UP!!","ALARM")
           break
def type(a):
    t.sleep(1.5)
    p.typewrite(a)

p.alert("System is live, please say 'activate' to engage with mainframe","{B.H.A.I}")

while True:

    text=user_audio()
    if text == "activate":
        speak("System Activated! Just ask me are you there")

        while True:

            text=user_audio()
            for i in range (len(desc)):
                if desc[i] in text:
                    intro()
            if "are you there" in text:
                speak("Yes hello! How can I help you")
            for i in range (len(exitkey)):
                if i<4:
                    if exitkey[i] in text:
                        speak("Would you like to exit?")
                        while True:
                            text=user_audio()
                            if "y" in text:
                                speak("Okay, It was nice talking to you, Goodbye!")
                                exit()
                            elif "no" in text:
                                speak("Okay")
                                break
                            else:
                                speak("please say yes or no")
                                continue
                else:
                    if exitkey[i] in text:
                        speak("Wow that's a rather strong approach, Would you like to exit?")
                        text=user_audio()
                        while True:
                            text=user_audio()
                            if "y" in text:
                                speak("Okay, It was nice talking to you, Goodbye!")
                                exit()
                            elif "no" in text:
                                speak("Okay")
                                break
                            else:
                                speak("please say yes or no")
                                continue
                    else:
                        pass
            if "alarm" in text:
                speak("Opening Alarm")
                alarmPrompt()
            if "i want to type" in text:
                a=user_audio()
                type(a)
            if "Unmute" in text:
                p.hotkey("alt","a")
                t.sleep(5)
                p.hotkey("alt","a")

    else:

        p.alert("Please say activate","{B.H.A.I}")










