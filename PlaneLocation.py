import requests
import keyboard
import os
import math


distance_km_val = 100

lamin = 0
lamax = 0
lomin = 0
lomax = 0

def calculate_bounds(lat, lon, distance_km = distance_km_val):
    lat_rad = math.radians(lat)

    delta_lat = distance_km / 111  # ~111 km per degree of latitude
    delta_lon = distance_km / (111 * math.cos(lat_rad))  # varies with latitude

    lamin = lat - delta_lat
    lamax = lat + delta_lat
    lomin = lon - delta_lon
    lomax = lon + delta_lon
    return round(lamin, 6), round(lamax, 6), round(lomin, 6), round(lomax, 6)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


lat, lon = 23.7993984, 90.423296
# delta = 0.1   # approx 11km or 11000 meter

lamin, lamax, lomin, lomax = calculate_bounds(lat, lon)

print("lamin: " , lamin , " lamax: " , lamax , " lomin: " , lomin , " lomax: " , lomax)
url = (
    f"https://opensky-network.org/api/states/all"
    f"?lamin={lamin}&lomin={lomin}"
    f"&lamax={lamax}&lomax={lomax}"
)

r = requests.get(url)
data = r.json()
count = 0
while True:
    if keyboard.is_pressed("q"):
        print("q pressed, ending loop")
        break

    if keyboard.is_pressed("e"):
        clear_terminal()
        print("terminal cleared")
    
    if not data.get("states"):
        print("No airborne flights within ~/s km.", distance_km_val)
    else:
        if count == 0:
            clear_terminal()
            count = count + 1

        print("Flights overhead:")
        print(data["states"])
        for s in data["states"]:
            print(f"- Callsign: {s[1] or 'N/A'}, Position: ({s[6]:.4f}, {s[5]:.4f}), "
                f"Alt: {s[7]} m, Speed: {s[9]:.1f} m/s")
            

