import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from gtts import gTTS
import playsound
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton, QGridLayout, QHBoxLayout, QLabel)
from PyQt5.QtGui import (QFont, QPainter, QColor)
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from translate import Translator


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("SWI AI")
        self.setFixedSize(600, 700)
        self.setWindowIcon(QtGui.QIcon('images/logos.png'))

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 300, 461, 81))
        self.label.setStyleSheet("color: lightgreen") 
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label1")


        self.me = QtWidgets.QLabel(self)
        self.me.setGeometry(QtCore.QRect(130, 170, 461, 81))
        self.me.setStyleSheet("color: blue") 
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.me.setFont(font)
        self.me.setObjectName("me")


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("speak")
        self.b1.setStyleSheet("color: blue") 
        font_button = QtGui.QFont()
        font_button.setPointSize(12)
        font_button.setBold(True)
        font_button.setWeight(75)
        self.b1.setFont(font_button)
        self.b1.setGeometry(QtCore.QRect(200, 450, 211, 71))
        self.b1.setStyleSheet("background-color : #C9F3FD") 
        self.b1.clicked.connect(self.clickedd)

     #   self.child = QWidget(self)
      #  self.child.setStyleSheet("background-color:red;border-radius:15px;")
       # self.child.setGeometry(300, 350, 15, 15)
        #self.anim = QPropertyAnimation(self.child, b"pos")
        #self.anim2 = QPropertyAnimation(self.child, b"pos")

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(270, 0, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("label1")
        self.title.setText("SWI")


        time.sleep(3)


    def animation1(self):
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setEndValue(QPoint(400, 350))
        self.anim.setDuration(1000)
        self.anim.start()




    def update(self):
        self.label.adjustSize()

    def ac(self):
        self.b1.setWindowOpacity(1)
        self.b1.setStyleSheet("background-color: AliceBlue")

    def aa(self):
        self.b1.setWindowOpacity(1)
        self.b1.setStyleSheet("background-color: #C9F3FD")

    def clickedd(self):
        self.b1 = self.sender() 
        QTimer.singleShot(1, self.ac)

        th1 = threading.Thread(target=self.smart)
        th1.start()

        QTimer.singleShot(100, self.aa)


    def smart(self):

            def speak(output):
                num=0
                print(output)
                num += 1
                response=gTTS(text=output, lang='en')
                file = str(num)+".mp3"
                response.save(file)
                playsound.playsound(file, True)
                os.remove(file)
                

            def takeCommand():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    said = ""

                    try:
                        said = r.recognize_google(audio)
                        print("me: " + said)
                        self.me.setText(said)
                    except Exception as e:
                        print("e")
                        said = "sasa"
                return said

            statement = takeCommand().lower()

            if "good bye" in statement or "bye" in statement or "stop" in statement or "shut up" in statement:
                time.sleep(0.5)
                self.label.setText('your personal assistant SWI is shutting down,\nGood bye!')
                self.label.adjustSize()
                speak('your personal assistant SWI is shutting down,Good bye!')
                sys.exit()

            elif "hello" in statement or "hie" in statement:
                time.sleep(0.5)
                self.label.setText("hello, you are in a good mood today? "+ "\npersonalaly i am.")
                self.label.adjustSize()
                speak('hello, you are in a good mood today? personalaly i am.')


            elif 'crazy' in statement or 'fuck' in statement or "whore" in statement or "f***" in statement:
                time.sleep(0.5)
                self.label.setText("it's not nice, I'm on strike")
                self.label.adjustSize()
                speak("it's not nice, I'm on strike")


            elif 'wikipedia' in statement:
                time.sleep(0.5)
                speak('Searching Wikipedia...')
                self.label.setText('Searching Wikipedia...')
                self.label.adjustSize()
                statement =statement.replace("Searching wikipedia", "")
                results = wikipedia.summary(statement, sentences=1)
                self.label.setText("According to Wikipedia")
                self.label.adjustSize()
                speak("According to Wikipedia")
                self.label.setText(results)
                self.label.adjustSize()
                speak(results)

            elif 'open youtube' in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://www.youtube.com")
                self.label.setText('youtube is open now')
                self.label.adjustSize()
                speak('youtube is open now.')
                time.sleep(5)

            elif 'open google' in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://www.google.com")
                self.label.setText("Google is open now.")
                self.label.adjustSize()
                speak("Google is open now.")
                time.sleep(5)

            elif 'open gmail' in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("gmail.com")
                self.label.setText("Google Mail open now")
                self.label.adjustSize()
                speak("Google Mail open now")
                time.sleep(5)

            elif 'what do you like' in statement:
                time.sleep(0.5)
                self.label.setText("I like help you")
                self.label.adjustSize()
                speak("I like help you")
                time.sleep(5)

            elif "weather" in statement:
                time.sleep(0.5)
                api_key="64f7f61815d3b00e86678284fcc41ff7"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                self.label.setText("whats the city name?")
                self.label.adjustSize()
                speak("whats the city name.")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    self.label.setText(" Temperature in kelvin unit is: " +
                          str(current_temperature) +
                          "\n humidity is: " +
                          str(current_humidiy) +"%" +
                          "\n description:  " +
                          str(weather_description))
                    self.label.adjustSize()
                    speak(" Temperature in kelvin unit is. " +
                          str(current_temperature) +
                          "\n .humidity is. " +
                          str(current_humidiy) +"percent"+
                          "\n .description.  " +
                          str(weather_description))

                else:
                    self.label.setText(" City Not Found in the database")
                    self.label.adjustSize()
                    speak(" City Not Found in the database")



            elif 'time' in statement:
                time.sleep(0.5)
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                self.label.setText(f"the time is {strTime}")
                self.label.adjustSize()
                speak(f"the time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                time.sleep(0.5)
                self.label.setText('I am SW1 version 1 point 1 your persoanl assistant. I am programmed to meet your needs')
                self.label.adjustSize()
                speak('I am SW1 version 1 point 1 your persoanl assistant. I am programmed to meet your needs')


            elif "made you" in statement or "created you" in statement or "discovered you" in statement:
                time.sleep(0.5)
                self.label.setText("I was built by vultorio")
                self.label.adjustSize()
                speak("I was built by vultorio")

            elif "open stackoverflow" in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                self.label.setText("Here is stackoverflow")
                self.label.adjustSize()
                speak("Here is stackoverflow")

            elif 'news' in statement:
                time.sleep(0.5)
                news = webbrowser.open_new_tab("https://www.bfmtv.com/")
                self.label.setText('Here are some headlines from the bfmtv sites.')
                self.label.adjustSize()
                speak('Here are some headlines from the bfmtv sites.')
                time.sleep(6)

            #francais : cette merde ne marche pas putaiiiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn =)
            #elif "camera" in statement or "take a photo" in statement:
                #ec.capture(0,"robo camera","img.jpg")

           # elif 'search'  in statement:
            #    statement = statement.replace("search", "")
             #   webbrowser.open_new_tab(statement)
              #  time.sleep(5)

            elif 'ask' in statement:
                time.sleep(0.5)
                self.label.setText('I can answer to computational and geographical \nquestions and what question do you want to ask now')
                self.label.adjustSize()
                speak('I can answer to computational and geographical questions and \nwhat question do you want to ask now')
                question=takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                self.label.setText(answer)
                self.label.adjustSize()
                speak(answer)


            elif "log off" in statement or "lof off on off" in statement:
                time.sleep(0.5)
                self.label.setText("Ok , your pc will log off in 10 sec make \nsure you exit from all applications")
                self.label.adjustSize()
                speak("Ok , your pc will log off in 10 sec make \nsure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "turn on" in statement or "tusdsdsdsdsdsdsdsdsdsdsdsdsdsdrn off" in statement:

                if "strip" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.64/control?cmd=gpio,12,0')
                    self.label.setText("strip led is turn on.")
                    self.label.adjustSize()
                    speak("strip led is turn on.")
                if "strip" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.64/control?cmd=gpio,15,0')
                    lf.label.setText("strip led is turn on.")
                    self.label.adjustSize()
                    speak("strip led is turn on.")

            elif "turn off" in statement or "tusdsdsdsdsdsdsdsdsdsdsdsdsdsdrn off" in statement:

                if "strip" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.64/control?cmd=gpio,12,1')
                    self.label.setText("strip led is turn off.")
                    self.label.adjustSize()
                    speak("strip led is turn off.")
                if "strip" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.64/control?cmd=gpio,15,1')
                    self.label.setText("strip led is turn off.")
                    self.label.adjustSize()
                    speak("strip led is turn off.")

            elif "do you like banana" in statement or "do you like bananas" in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=ef-P_sC-_0c&ab_channel=JenNard")
                self.label.setText("I think that expresses my answer")
                self.label.adjustSize()
                speak("I think that expresses my answer")

            elif "definition of" in statement:
                time.sleep(0.5)
                statement =statement.replace("definition of", "")
                results = wikipedia.summary(statement, sentences=1)
                self.label.setText(results)
                self.label.adjustSize()
                speak(results)

            elif "what's mean" in statement:
                statement = statement.replace("what's mean", "")
                print(statement)
                self.label.setText("in which language do you want to translate?")
                self.label.adjustSize()
                speak("in which language do you want to translate?")
                language=takeCommand()
                language = language.replace("in French", "french")
                translator= Translator(from_lang="english",to_lang=language)
                translation = translator.translate(statement)
                print (translation)
                self.label.setText(statement+" in "+language+" mean with \nmy english accent"+translation)
                self.label.adjustSize()
                speak(statement+" in "+language+" mean with my english accent"+translation)


            else:
                if statement != "sasa":
                    time.sleep(0.5)
                    webbrowser.open_new_tab(statement)
                    self.label.setText("here is what I found on the web for:\n" + statement)
                    self.label.adjustSize()
                    speak("here is what I found on the web for: " + statement)
                    time.sleep(5)



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()    
