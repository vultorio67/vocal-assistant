@echo off
echo would you like install pyaudio
set /p py=
if %py%==yes ( py -m pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl) else (echo bye)
pause>nul