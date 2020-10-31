# OneStopLogs
OneStopLogs provides a script that is able to determine your machine's OS (Windows or Linux) and collect the logs accordingly. <br/>
OneStopLogs also provides a web application that is able to analyse and visualise the logs that were collected from the script.

Currently working OS versions:<br/>
Windows 10<br/>
Linux (Kali)<br/>
Linux (Ubuntu)

## Installation
For installation: <br/>
The web application runs on python flask specifically python3<br/>
You are also required to pip3 install the following:<br/>
Flask<br/>
Werkzeug

## Usage
**Files(onestoplogs.bat & onestoplogs.ps1) in /Scripts must be in the same directory of your choosing**

Windows:<br/>
Double click on the bat file<br/>
You will be prompted for UAC elevation twice, click yes both times <br/>
Files extracted will be in the same directory as the bat file. ({.bat Directory}/temp/logs/windows/{today's date})<br/>

*Windows Operating System automatically blocks scripts downloaded from the internet to help protect the computer. However, we have found a workaround and are able to unblock the script from bash. <br/>

*By default, Windows Operating System will set a user’s Execution-Policy to be restricted. This causes a problem for us as we are unable to run scripts on the machine. However, there is no need to manually change the Execution-Policy of the current user as we have found a way to bypass and elevate the Execution-Policy from restricted to remote access. After the execution of our scripts, we will demote the Execution-Policy of the user back to restricted. <br/>

Linux:<br/>
Open up a terminal in the directory where the .bat file is<br/>
chmod 777 onestoplogs.bat (to provide permissions to execute the script)<br/>
./onestoplogs.bat (run the script)<br/>
Files extracted will be in the same directory as the bat file. ({.bat Directory}/temp/logs/linux/{today's date})<br/>

Once the logs have been extracted<br/>
Run the webapp.py<br/>
Open a web browser and type in 127.0.0.1:5000<br/>
Insert the file path of the logs into the text box ({.bat Directory}/temp/logs/linux/{today's date})

## Team Members
Tay Qi Wen Jordan (1902114)<br/>
Poh Hong Yi (1902148)<br/>
Poh Qi Xian Bryan (1902197)<br/>
Lee Khai Liang Eugene (1902155)
