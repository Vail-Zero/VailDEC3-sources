@echo off
cd ./
pyinstaller VailDEC.spec --exclude-module numpy --exclude-module pandas
pause