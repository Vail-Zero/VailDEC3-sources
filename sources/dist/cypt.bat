@echo off
cd ./

SignTool sign /fd sha256 /a /T http://timestamp.digicert.com /f msen.pfx /p "divingsparrow" VailDEC.exe
pause