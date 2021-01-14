import json
from gtts import gTTS
import speech_recognition as sr
import playsound
import os
from ast import literal_eval


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
        except Exception as e:
            print("e")
            said = "sasa"
            speak("Sorry I didn't understand")
    return said



def exist():
	try:
	    My_file=open('info.json')
	    My_file.close()
	    print("File found!")
	    isExist = True
	except FileNotFoundError:
	    print("Files not exist")
	    isExist = False

	if isExist == False:
	    get_info()

infoFile = "info.json"

def get_info():
	file = open("info.json", "w+")
	isi = True
	speak("what is your name?")
	statement = takeCommand().lower()
	statement = statement.replace("my name is", "")
	sName = statement
	print(sName)
	speak("How old are you?")
	statement = takeCommand().lower()
	statement = statement.replace("i am", "")
	sAge = statement
	print(sAge)
	speak("What is your country?")
	statement = takeCommand().lower()
	statement = statement.replace("my country is", "")
	sCountry = statement
	print(sCountry)

	def write_info(name, age, country):

		with open(infoFile, 'w') as file:
			json.dump(str({"name": name, "age": age, "country": country}), file)

	write_info(sName, sAge, sCountry)

def read_info(what):
	with open(infoFile, 'r') as file:
		uInfo = json.load(file)
		uInfo = literal_eval(uInfo)
		uInfo = uInfo[what]
		return uInfo






