@echo off

:check_connection
cls
echo Check Internet connection...
curl -s --head http://www.baidu.com | findstr /i "HTTP/1.1 200" >nul
if errorlevel 1 (
    echo No valid connection, restart check in 10 seconds...
    timeout /t 10 >nul
    goto check_connection
)

echo Start running script...

set PASSWORD=040218
wsl bash -c "echo %PASSWORD% | sudo -S mount -o remount,rw '/tmp/.X11-unix' && echo %PASSWORD% | sudo -S chmod 1777 /tmp/.X11-unix"
cls
wsl bash -c "source /home/kusicfack/venv/bin/activate && cd /home/kusicfack/Auto_Signer && python3 main.py"

pause

wsl --shutdown