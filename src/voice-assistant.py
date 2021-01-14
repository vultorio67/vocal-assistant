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
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import translate
import info


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
        self.setFixedSize(500, 650)
        self.setWindowIcon(QtGui.QIcon('images/logos.png'))

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(225, 0, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("SWI")
        self.title.setText("SWI")

        self.me = QtWidgets.QLabel(self)
        self.me.setGeometry(QtCore.QRect(50, 170, 400, 81))
        self.me.setStyleSheet("color: #F14800") 
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.me.setFont(font)
        self.me.setObjectName("me")


        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 300, 400, 81))
        self.label.setStyleSheet("color: lightgreen") 
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label1")


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("speak")
        font_button = QtGui.QFont()
        font_button.setPointSize(12)
        font_button.setBold(True)
        font_button.setWeight(75)
        self.b1.setStyleSheet("background-color: #0B4C5F;")
        self.b1.setFont(font_button)
        self.b1.setGeometry(QtCore.QRect(150, 500, 211, 71))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.clickedd)

        #transform = QTransform()
        #transform.scale(self.b1, 2.2, 2.2)
        #b1.setTransform(transform)


     #   self.child = QWidget(self)
      #  self.child.setStyleSheet("background-color:red;border-radius:15px;")
       # self.child.setGeometry(300, 350, 15, 15)
        #self.anim = QPropertyAnimation(self.child, b"pos")
        #self.anim2 = QPropertyAnimation(self.child, b"pos")


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
        self.b1.setStyleSheet("background-color: #0B4C5F")

    def aa(self):
        self.b1.setWindowOpacity(1)
        self.b1.setStyleSheet("background-color: #01DF3A")

    def clickedd(self):
        self.b1 = self.sender() 
        QTimer.singleShot(100, self.ac)

        th1 = threading.Thread(target=self.smart)
        th1.start()
        QTimer.singleShot(1, self.aa)




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

                info.exist()

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
                        self.label.setText("Sorry I didn't understand")
                        speak("Sorry I didn't understand")
                return said

            statement = takeCommand().lower()

            if "good bye" in statement or "bye" in statement or "stop" in statement or "shut up" in statement:
                time.sleep(0.5)
                self.label.setText('your personal assistant SWI is shutting down,\nGood bye!')
                speak('your personal assistant SWI is shutting down,Good bye!')
                sys.exit()

            elif "hello" in statement or "hie" in statement:
                tName = info.read_info('name')
                time.sleep(0.5)
                self.label.setText("hello " + tName +", \nhow can i help you?")
                speak('hello ' + tName +', how can i help you?')


            elif 'crazy' in statement or 'fuck' in statement or "whore" in statement or "f***" in statement:
                time.sleep(0.5)
                self.label.setText("it's not nice, I'm on strike")
                speak("it's not nice, I'm on strike")


            elif 'wikipedia' in statement:
                time.sleep(0.5)
                speak('Searching Wikipedia...')
                self.label.setText('Searching Wikipedia...')
                statement =statement.replace("Searching wikipedia", "")
                results = wikipedia.summary(statement, sentences=1)
                self.label.setText("According to Wikipedia")
                speak("According to Wikipedia")
                self.label.setText(results)
                speak(results)

            elif 'youtube' in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://www.youtube.com")
                self.label.setText('youtube is open now')
                speak('youtube is open now.')
                time.sleep(5)

            elif 'google' in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://www.google.com")
                self.label.setText("Google is open now.")
                speak("Google is open now.")
                time.sleep(5)

            elif 'gmail' in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("gmail.com")
                self.label.setText("Google Mail open now")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'what do you like' in statement:
                time.sleep(0.5)
                self.label.setText("I like help you")
                speak("I like help you")
                time.sleep(5)


            elif "weather" in statement:
                time.sleep(0.5)
                api_key="64f7f61815d3b00e86678284fcc41ff7"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                self.label.setText("whats the city name?")
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
                    speak(" City Not Found in the database")



            elif 'time' in statement:
                time.sleep(0.5)
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                self.label.setText(f"the time is {strTime}")
                speak(f"the time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                time.sleep(0.5)
                self.label.setText('I am SW1 version 1 point 1 your persoanl assistant. I am programmed to meet your needs')
                speak('I am SW1 version 1 point 1 your persoanl assistant. I am programmed to meet your needs')


            elif "made you" in statement or "created you" in statement or "discovered you" in statement:
                time.sleep(0.5)
                self.label.setText("I was built by vultorio")
                speak("I was built by vultorio")

            elif "open stackoverflow" in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                self.label.setText("Here is stackoverflow")
                speak("Here is stackoverflow")

            elif 'news' in statement:
                time.sleep(0.5)
                news = webbrowser.open_new_tab("https://www.bfmtv.com/")
                self.label.setText('Here are some headlines from the bfmtv sites.')
                speak('Here are some headlines from the bfmtv sites.')
                time.sleep(6)

           # elif 'search'  in statement:
            #    statement = statement.replace("search", "")
             #   webbrowser.open_new_tab(statement)
              #  time.sleep(5)

            elif 'ask' in statement:
                time.sleep(0.5)
                self.label.setText('I can answer to computational and geographical \nquestions and what question do you want to ask now')
                speak('I can answer to computational and geographical questions and \nwhat question do you want to ask now')
                question=takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                self.label.setText(answer)
                speak(answer)


            elif "log off" in statement or "lof off on off" in statement:
                time.sleep(0.5)
                self.label.setText("Ok , your pc will log off in 10 sec make \nsure you exit from all applications")
                speak("Ok , your pc will log off in 10 sec make \nsure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "turn on" in statement:

                if "strip" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.66/control?cmd=gpio,0,0')
                    self.label.setText("strip led is turn on.")
                    speak("strip led is turn on.")
                if "back" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.66/control?cmd=gpio,0,1')
                    lf.label.setText("strip led is turn on.")
                    speak("strip led is turn on.")

            elif "turn off" in statement:

                if "strip" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.66/control?cmd=gpio,13,0')
                    self.label.setText("strip led is turn off.")
                    speak("strip led is turn off.")
                if "back" in statement :
                    time.sleep(0.5)
                    x = requests.get('http://192.168.1.66/control?cmd=gpio,13,1')
                    self.label.setText("strip led is turn off.")
                    speak("strip led is turn off.")

            elif "do you like banana" in statement or "do you like bananas" in statement:
                time.sleep(0.5)
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=ef-P_sC-_0c&ab_channel=JenNard")
                self.label.setText("I think that expresses my answer")
                speak("I think that expresses my answer")

            elif "definition of" in statement:
                time.sleep(0.5)
                statement =statement.replace("definition of", "")
                results = wikipedia.summary(statement, sentences=1)
                self.label.setText(results)
                speak(results)

            elif "what's mean" in statement:
                statement = statement.replace("what's mean", "")
                print(statement)
                self.label.setText("in which language do you want to translate?")
                speak("in which language do you want to translate?")
                language=takeCommand()
                language = language.replace("in", "")
                translator= Translator(from_lang="english",to_lang=language)
                translation = translator.translate(statement)
                print (translation)
                self.label.setText(statement+" in "+language+" mean with \nmy english accent"+translation)
                speak(statement+" in "+language+" mean with my english accent"+translation)


            elif "translate" in statement:
            	#if "in" in statement:
            		
                statement = statement.replace("translate", "")
                print(statement)
                self.label.setText("in which language do you want to translate?")
                speak("in which language do you want to translate?")
                language=takeCommand()
                language = language.replace("in", "")
                translator= Translator(from_lang="english",to_lang=language)
                translation = translator.translate(statement)
                print (translation)
                self.label.setText(statement+" in "+language+" mean with \nmy english accent"+translation)
                speak(statement+" in "+language+" mean with my english accent"+translation)


            else:
                if statement != "sasa":
                    time.sleep(0.5)
                    webbrowser.open_new_tab(statement)
                    self.label.setText("here is what I found on the web for:\n" + statement)
                    speak("here is what I found on the web for: " + statement)
                    time.sleep(5)



def window():
    app = QApplication(sys.argv)
    style = """
    	QWidget{
    		background: #051233
    	}
    	QLabel#SWI{
    		color: #0EDFFB;
    	}
    	QPushButton#b1
    	{
    		color: #045FB4;
    		background-color: #0B4C5F;
    		border-style: outset;
		    border-width: 2px;
		    border-radius: 10px;
		    border-color: #2E2E2E;
    	}
    	QPushButton#b1:hover
    	{
    		transform = QTransform()
    		color: #00FF40;
    	}

    	QLabel#label1
    	{
		    background-color: #610B0B;
		    border-style: outset;
		    border-width: 2px;
		    border-radius: 10px;
		    border-color: beige;
		    font: bold 14px;
		    min-width: 10em;
		    padding: 6px;
    	}
    	   QLabel#me
    	{
		    background-color: #0B6121;
		    border-style: outset;
		    border-width: 2px;
		    border-radius: 10px;
		    border-color: beige;
		    font: bold 14px;
		    min-width: 10em;
		    padding: 6px;
    	}
    """
    app.setStyleSheet(style)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()   