@echo off
echo if "py command not found" please install python 3.8 : https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe
echo
echo Do you agree to install this package: SpeechRecognition, pyttsx3, wikipedia, wolframalpha, gTTS, playsound, pygt5
echo "yes" or "not"
set /p chiffre=
if %chiffre%==yes (
	echo installing package...
	echo
	py -m pip install SpeechRecognition
	py -m pip install pyttsx3
	py -m pip install wikipedia
	py -m pip install pygt5
	py -m pip install wolframalpha
	py -m pip install gTTS
	py -m pip install playsound
	py -m pip install pyaudio
	echo
	echo if pyaudio installation did not work please run "pyaudio.bat"
	) else (echo the program will not working!!!) 
pause>nul