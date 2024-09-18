@echo off
color 0A
title Filter Evaluation 
if EXIST .\venv GOTO CHECKDBPW
echo creating virtual environment: venv
python -m venv venv
echo activating virtual environment and updating pip in venv
cmd /C ".\venv\Scripts\activate & python -m pip install --upgrade pip"
echo installing required modules from requirements.txt into venv
cmd /C ".\venv\Scripts\activate & python -m pip install -r requirements.txt" 
:CHECKDBPW
echo activating virtual environment: venv
cmd /K ".\venv\Scripts\activate & echo start test server with python app.py"
exit