$today = Get-Date -format "yyyyMMdd"
$P = $args[0]
mkdir $P\temp\logs\windows\$today | Out-Null

$filename = "$P\temp\logs\windows\$today\Recent.csv"
dir $env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Recent| Export-Csv $filename

$filename = "$P\temp\logs\windows\$today\prefetch.csv"
dir C:\Windows\Prefetch| Export-Csv $filename

$filename = "$P\temp\logs\windows\$today\Application.csv"
Get-EventLog Application -After (get-date).addDays(-7) | Export-CSV $filename


$filename = "$P\temp\logs\windows\$today\System.csv"
Get-EventLog System -After (get-date).addDays(-7) | Export-CSV $filename


$filename = "$P\temp\logs\windows\$today\Security.csv"
Get-EventLog Security -After (get-date).addDays(-7) | Export-CSV $filename

$LSM = @{
    LogName="Microsoft-Windows-TerminalServices-LocalSessionManager/Operational"
    StartTime=((get-date).addDays(-7))
}

$filename = "$P\temp\logs\windows\$today\TerminalServices-LocalSessionManager.csv"
Get-WinEvent -FilterHashtable $LSM |Export-CSV $filename
