import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import app
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
from PyQt5.uic.properties import QtCore, QtGui
from gtts import gTTS
import playsound
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from translate import Translator
from covid import Covid
from PyQt5.QtGui import *
import translate
import matplotlib.pyplot as pyplot
from PyQt5.QtCore import *
from PyQt5 import *
import json
import pyttsx3
import getInfo

# GUI FILE
from app import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.saidbis = None
        self.ui.setupUi(self)
        self.ui.b1.clicked.connect(self.hello)
        self.show()

    def hello(self):
        th1 = threading.Thread(target=self.smart)
        th1.start()

    def smart(self):
        print("hello")
        if self.saidbis == self.ui.me.text():
            self.ui.me.setText("")

        def speak(output):
            num = 0
            print(output)
            num += 1
            response = gTTS(text=output, lang='en')
            file = str(num) + ".mp3"
            response.save(file)
            playsound.playsound(file, True)
            os.remove(file)

        def takeCommand():
            getInfo.exist()

            print(self.ui.me.text())

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""

                try:
                    said = r.recognize_google(audio)
                    print(said)
                    self.ui.me.setText(said)
                except Exception as e:
                    print("e")
                    said = False
                    self.ui.label.setText("Sorry I didn't understand")
                    speak("Sorry I didn't understand")
            return said

        if self.ui.me.text() == "":
            statement = takeCommand()

        else:
            self.saidbis = self.ui.me.text()
            statement = self.ui.me.text()

        if "good bye" in statement or "bye" in statement or "stop" in statement or "shut up" in statement:
            time.sleep(0.5)
            self.ui.label.setText('your personal assistant SWI is shutting down,\nGood bye!')
            speak('your personal assistant SWI is shutting down,Good bye!')

        elif "hello" in statement or "hie" in statement:
            tName = getInfo.read_info('name')
            time.sleep(0.5)
            self.ui.label.setText("hello " + tName + ", \nhow can i help you?")
            speak('hello ' + tName + ', how can i help you?')

        elif "me" and "know" in statement:
            self.ui.label.setText("this is what i know about you. \nYour name is " + getInfo.read_info(
                'name') + ", you have " + getInfo.read_info('age') +
                               " years old, \nyou leave in " + getInfo.read_info('country'))

            speak("this is what i know about you. \nYour name is " + getInfo.read_info(
                'name') + ", you have " + getInfo.read_info('age') +
                  " years old, \nyou leave in " + getInfo.read_info('country'))



        elif 'crazy' in statement or 'fuck' in statement or "whore" in statement or "f***" in statement:
            time.sleep(0.5)
            self.ui.label.setText("it's not nice, I'm on strike")
            speak("it's not nice, I'm on strike")


        elif 'wikipedia' in statement:
            time.sleep(0.5)
            speak('Searching Wikipedia...')
            self.ui.label.setText('Searching Wikipedia...')
            statement = statement.replace("Searching wikipedia", "")
            results = wikipedia.summary(statement, sentences=1)
            self.ui.label.setText("According to Wikipedia")
            speak("According to Wikipedia")
            self.ui.label.setText(results)
            speak(results)

        elif 'youtube' in statement:
            time.sleep(0.5)
            webbrowser.open_new_tab("https://www.youtube.com")
            self.ui.label.setText('youtube is open now')
            speak('youtube is open now.')
            time.sleep(5)

        elif 'google' in statement:
            time.sleep(0.5)
            webbrowser.open_new_tab("https://www.google.com")
            self.ui.label.setText("Google is open now.")
            speak("Google is open now.")
            time.sleep(5)

        elif 'gmail' in statement:
            time.sleep(0.5)
            webbrowser.open_new_tab("gmail.com")
            self.ui.label.setText("Google Mail open now")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'what' and 'like' in statement:
            time.sleep(0.5)
            self.ui.label.setText("I like help you")
            speak("I like help you")
            time.sleep(5)


        elif "weather" in statement:
            time.sleep(0.5)
            api_key = "64f7f61815d3b00e86678284fcc41ff7"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            self.ui.label.setText("whats the city name?")
            speak("whats the city name.")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                self.ui.label.setText(" Temperature in kelvin unit is: " +
                                   str(current_temperature) +
                                   "\n humidity is: " +
                                   str(current_humidiy) + "%" +
                                   "\n description:  " +
                                   str(weather_description))
                self.ui.label.adjustSize()
                speak(" Temperature in kelvin unit is. " +
                      str(current_temperature) +
                      "\n .humidity is. " +
                      str(current_humidiy) + "percent" +
                      "\n .description.  " +
                      str(weather_description))

            else:
                self.ui.label.setText(" City Not Found in the database")
                speak(" City Not Found in the database")



        elif 'time' in statement:
            time.sleep(0.5)
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            self.ui.label.setText(f"the time is {strTime}")
            speak(f"the time is {strTime}")

        elif 'who' and 'you' in statement or 'what' and 'do' in statement:
            time.sleep(0.5)
            self.ui.label.setText('I am SW1 version 1.2 your persoanl assistant. \nI am programmed to meet your needs')
            speak('I am SW1 version 1 point 2 your persoanl assistant. I am programmed to meet your needs')


        elif "made you" in statement or "created you" in statement or "discovered you" in statement:
            time.sleep(0.5)
            self.ui.label.setText("I was built by vultorio")
            speak("I was built by vultorio")

        elif "stackoverflow" in statement:
            time.sleep(0.5)
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            self.ui.label.setText("Here is stackoverflow")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            time.sleep(0.5)
            news = webbrowser.open_new_tab("https://www.bfmtv.com/")
            self.ui.label.setText('Here are some headlines from the bfmtv sites.')
            speak('Here are some headlines from the bfmtv sites.')
            time.sleep(6)

        # elif 'search'  in statement:
        #    statement = statement.replace("search", "")
        #   webbrowser.open_new_tab(statement)
        #  time.sleep(5)

        elif 'ask' in statement:
            time.sleep(0.5)
            self.ui.label.setText(
                'I can answer to computational and geographical \nquestions and what question do you want to ask now')
            speak('I can answer to computational and geographical questions and \nwhat question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            self.ui.label.setText(answer)
            speak(answer)


        elif "log off" in statement or "lof off on off" in statement:
            time.sleep(0.5)
            self.ui.label.setText("Ok , your pc will log off in 10 sec make \nsure you exit from all applications")
            speak("Ok , your pc will log off in 10 sec make \nsure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "turn on" in statement:

            if "strip" in statement:
                time.sleep(0.5)
                x = requests.get('http://192.168.1.66/control?cmd=gpio,0,0')
                self.ui.label.setText("strip led is turn on.")
                speak("strip led is turn on.")
            if "back" in statement:
                time.sleep(0.5)
                x = requests.get('http://192.168.1.66/control?cmd=gpio,0,1')
                self.ui.label.setText("strip led is turn on.")
                speak("strip led is turn on.")

        elif "turn off" in statement:

            if "strip" in statement:
                time.sleep(0.5)
                x = requests.get('http://192.168.1.66/control?cmd=gpio,13,0')
                self.ui.label.setText("strip led is turn off.")
                speak("strip led is turn off.")
            if "back" in statement:
                time.sleep(0.5)
                x = requests.get('http://192.168.1.66/control?cmd=gpio,13,1')
                self.ui.label.setText("strip led is turn off.")
                speak("strip led is turn off.")

        elif "do you like banana" in statement or "do you like bananas" in statement:
            time.sleep(0.5)
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=ef-P_sC-_0c&ab_channel=JenNard")
            self.ui.label.setText("I think that expresses my answer")
            speak("I think that expresses my answer")

        elif "definition of" in statement:
            time.sleep(0.5)
            statement = statement.replace("definition of", "")
            results = wikipedia.summary(statement, sentences=1)
            self.ui.label.setText(results)
            speak(results)

        elif "what" in statement:
            self.ui.label.setText("what, what")
            speak("what? what.")

        elif "translate" in statement or "what's mean" in statement:

            if "in" in statement:
                if "in french" in statement:
                    language = "french"
                if "in german" in statement:
                    language = "german"
                if "in spanish" in statement:
                    language = "spanish"
                print("hello")
                statement = statement.replace("translate", "")
                statement = statement.replace("what's mean", "")
                statement = statement.replace("in german", "")
                statement = statement.replace("in french", "")
                statement = statement.replace("in spanish", "")
                print(statement)
                translator = Translator(from_lang="english", to_lang=language)
                translation = translator.translate(statement)
                print(translation)
                self.ui.label.setText(statement + " in " + language + " mean with \nmy english accent " + translation)
                speak(statement + " in " + language + " mean with my english accent " + translation)

            else:
                statement = statement.replace("translate", "")
                statement = statement.replace("what's mean", "")
                print(statement)
                self.ui.label.setText("in witch languge do you want to translate?")
                speak("in witch languge do you want to translate?")
                statement = takeCommand().lower()
                language = statement
                translator = Translator(from_lang="english", to_lang=statement)
                translation = translator.translate(statement)
                print(translation)
                self.ui.label.setText(statement + " in " + language + " mean with \nmy english accent " + translation)
                speak(statement + " in " + language + " mean with my english accent " + translation)






        else:
            if statement != "False":
                time.sleep(0.5)
                webbrowser.open_new_tab(statement)
                self.ui.label.setText("here is what I found on the web for:\n" + statement)
                speak("here is what I found on the web for: " + statement)


    def resizeMainWindow(self, width, height):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QtCore.QSize(width,height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
