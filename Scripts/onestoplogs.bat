#|| goto :batch_part
  #get media directory
  OUTPUT=$(pwd) 
  #get today's date
  OUTPUT1=$(date +%Y%m%d)
  
  #make directory
  mkdir -p ${OUTPUT}/temp/logs/linux/${OUTPUT1}/

  #getting 4 log files (auth, syslog, messages, kern)
  #formatting the file (column headers)
  #fetching the logs and adding to file
  < /var/log/auth.log awk '{if(NR==1){print "Date| Hostname| Service| Message";}else{printf $2" "$1" "$3 " | " $4 " | " $5 " | "; s = ""; for (i = 6; i <= NF; i++) s = s $i " "; print s "|"}}' >> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/authLogs.csv
  < /var/log/syslog awk '{if(NR==1){print "Date| Hostname| Service| Message";}else{printf $2" "$1" "$3 " | " $4 " | " $5 " | "; s = ""; for (i = 6; i <= NF; i++) s = s $i " "; print s "|"}}' >> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/sysLogs.csv
  < /var/log/messages awk '{if(NR==1){print "Date| Hostname| Service| Message";}else{printf $2" "$1" "$3 " | " $4 " | " $5 " | "; s = ""; for (i = 6; i <= NF; i++) s = s $i " "; print s "|"}}' >> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/messagesLogs.csv
  < /var/log/kern.log awk '{if(NR==1){print "Date| Hostname| Service| Message";}else{printf $2" "$1" "$3 " | " $4 " | " $5 " | "; s = ""; for (i = 6; i <= NF; i++) s = s $i " "; print s "|"}}' >> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/kernLogs.csv
  
  #getting last logins from users who log in within 7 days
  lastlog -b 0 -t 7 | awk '{printf $1"| "$2"| "$3 " | "; s = ""; for (i = 4; i <= NF; i++) s = s $i " "; print s "|"}'> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/lastLog.csv


  #getting history(command) of all users and root
  #make directory
  mkdir -p ${OUTPUT}/temp/logs/linux/${OUTPUT1}/history
  mkdir -p ${OUTPUT}/temp/logs/linux/${OUTPUT1}/last
  mkdir -p ${OUTPUT}/temp/logs/linux/${OUTPUT1}/lastb
  #root .bash_history comes with timestamp
  cat /root/.bash_history > ${OUTPUT}/temp/logs/linux/${OUTPUT1}/history/root.txt
  last root -F | awk '{printf $1"|" $2"|" $3"|"; s = ""; for (i = 4; i <= NF; i++) s = s $i " "; print s"|"}' > ${OUTPUT}/temp/logs/linux/${OUTPUT1}/last/root.txt
  lastb root -F | awk '{printf $1"|" $2"|" $3"|"; s = ""; for (i = 4; i <= NF; i++) s = s $i " "; print s"|"}' > ${OUTPUT}/temp/logs/linux/${OUTPUT1}/lastb/root.txt
  #find all users and loop their history

  Users=$(getent passwd {1000..6000} | cut -d: -f1)
  for i in ${Users}
	do
  		cat /home/$i/.bash_history > ${OUTPUT}/temp/logs/linux/${OUTPUT1}/history/$i.txt
                last $i -F | awk '{printf $1"|" $2"|" $3"|"; s = ""; for (i = 4; i <= NF; i++) s = s $i " "; print s"|"}' > ${OUTPUT}/temp/logs/linux/${OUTPUT1}/last/$i.txt
		lastb $i -F | awk '{printf $1"|" $2"|" $3"|"; s = ""; for (i = 4; i <= NF; i++) s = s $i " "; print s"|"}' > ${OUTPUT}/temp/logs/linux/${OUTPUT1}/lastb/$i.txt
	done

   #store list of users to a txt file
   echo "root" >> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/userList.txt
   getent passwd {1000..6000} | cut -d: -f1 >> ${OUTPUT}/temp/logs/linux/${OUTPUT1}/userList.txt
exit

:batch_part
 @ECHO OFF  
 echo "Detected Linux OS"
 PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force' -Verb RunAs}"
 powershell.exe  -Command  "Unblock-File -Path %cd%/onestoplogs.ps1"
 powershell.exe  -Command  "Start-Process  powershell -argument '%cd%/onestoplogs.ps1 %cd%' -verb runas"
 PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList 'Set-ExecutionPolicy Restricted -Scope CurrentUser -Force' -Verb RunAs}"

