# OneStopLogs
OneStopLogs provides a script that is able to determine your machine's OS (Windows or Linux) and collect the logs accordingly. <br/>
OneStopLogs also provides a web application that is able to analyse and visualise the logs that were collected from the script.

## Installation
For installation:
The web application runs on python flask specifically python3
You are also required to pip3 install the following:
Flask
Werkzeug

## Usage
**Files(onestoplogs.bat & onestoplogs.ps1) in /Scripts must be in the same directory of your choosing

Windows:
Right click the onestoplogs.ps1 > properties > General > uncheck the Unblock checkbox (powershell scripts that are downloaded can be blocked by windows)
Double click on the bat file
You will be prompted for UAC elevation twice, click yes both times 
Files extracted will be in the same directory as the bat file. ({.bat Directory}/temp/logs/windows/{today's date})

Linux:
Open up a terminal in the directory where the .bat file is
chmod 777 onestoplogs.bat (to provide permissions to execute the script)
./onestoplogs.bat (run the script)
Files extracted will be in the same directory as the bat file. ({.bat Directory}/temp/logs/linux/{today's date})

Once the logs have been extracted
Run the webapp.py
Open a web browser and type in 127.0.0.1:5000
Insert the file path of the logs into the text box ({.bat Directory}/temp/logs/linux/{today's date})

## Team Members
Tay Qi Wen Jordan (1902114)
Poh Hong Yi (1902148)
Poh Qi Xian Bryan (1902197)
Lee Khai Liang Eugene (1902155)
