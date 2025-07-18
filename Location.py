import subprocess
import re
import json
import requests

API_KEY = "Your Api Key"   #google cloud

def is_valid_mac(mac):
    return re.match(r"^([0-9a-f]{2}:){5}[0-9a-f]{2}$", mac.lower()) is not None

def scan_wifi():
    print("\n Running netsh...")
    cmd_output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode("utf-8", errors="ignore")
    print("\n === Raw netsh Output ===\n")
    print(cmd_output)

    networks = []
    current_bssid = None

    print("\n Parsing networks...\n")
    for line in cmd_output.splitlines():
        line = line.strip()

        if line.startswith("BSSID"):
            raw_mac = line.split(":", 1)[-1].strip()
            mac = raw_mac.replace("-", ":").lower()
            print(f"Found BSSID line: {raw_mac} → Parsed MAC: {mac}")
            if is_valid_mac(mac):
                current_bssid = mac
            else:
                print(f"Invalid MAC: {mac}")
                current_bssid = None

        elif line.startswith("Signal") and current_bssid:
            try:
                percent = int(line.split(":")[-1].replace("%", "").strip())
                strength_dbm = int(-100 + (percent * 0.5))
                networks.append({
                    "macAddress": current_bssid,
                    "signalStrength": strength_dbm
                })
                print(f"Added: {current_bssid} with strength {strength_dbm} dBm")
            except Exception as e:
                print(f"Error parsing signal: {e}")
            current_bssid = None

    print(f"\n Parsed Networks:\n{json.dumps(networks, indent=4)}\n")
    return networks

def get_location(wifi_data):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"
    payload = {
        "considerIp": True,
        "wifiAccessPoints": wifi_data
    }
    response = requests.post(url, json=payload)
    return response.json()

# Run
wifi_info = scan_wifi()
if not wifi_info:
    print("No valid Wi-Fi networks parsed.")
else:
    print("Requesting location from Google...\n")
    location = get_location(wifi_info)
    print(json.dumps(location, indent=4))
