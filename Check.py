import wmi

def check_gps_devices():
    c = wmi.WMI()
    gps_found = False
    for item in c.Win32_PnPEntity():
        if item.Name and "GPS" in item.Name.upper():
            print(f"GPS device found: {item.Name}")
            gps_found = True
    if not gps_found:
        print("No GPS device found.")

# check_gps_devices()
import subprocess

try:
    output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode()
    print("=== netsh output ===")
    print(output)
except subprocess.CalledProcessError as e:
    print("Error running netsh:", e.output.decode())

