@ECHO OFF

REM You should automate this script to run regularly

set scriptpath=%~dp0
cd %scriptpath%
call python src\main.py
