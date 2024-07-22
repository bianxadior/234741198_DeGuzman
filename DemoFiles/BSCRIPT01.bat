@echo off

REM Open five websites including Google, Facebook, YouTube, Instagram and Pinterest
start https://www.google.com
start https://www.facebook.com
start https://www.youtube.com
start https://www.instagram.com
start https://www.pinterest.com

REM Launch calculator and notepad
start calc
start notepad

REM Initiate a system shutdown after a brief delay.
timeout /t 60 /nobreak
shutdown /s /f /t 10 

exit
