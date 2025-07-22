import threading
import requests
import keyboard
import os
import math
import time

# Global control flag
running = True

lat, lon = 23.7993984, 90.423296   
distance_km_val = 100

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_bounds(lat, lon, distance_km = distance_km_val):
    lat_rad = math.radians(lat)

    delta_lat = distance_km / 111  # ~111 km per degree of latitude
    delta_lon = distance_km / (111 * math.cos(lat_rad))  # varies with latitude

    lamin = lat - delta_lat
    lamax = lat + delta_lat
    lomin = lon - delta_lon
    lomax = lon + delta_lon
    return round(lamin, 6), round(lamax, 6), round(lomin, 6), round(lomax, 6)


def getPlaneInfo():
    r = requests.get(url)
    data = r.json()
    count = 0
    
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
   
            
lamin, lamax, lomin, lomax = calculate_bounds(lat, lon)
print("lamin: " , lamin , " lamax: " , lamax , " lomin: " , lomin , " lomax: " , lomax)

url = (
    f"https://opensky-network.org/api/states/all"
    f"?lamin={lamin}&lomin={lomin}"
    f"&lamax={lamax}&lomax={lomax}"
)

def keyboard_listener():
    global running
    while running:
        if keyboard.is_pressed("q"):
            print("q pressed, exiting program.")
            running = False
            break
        if keyboard.is_pressed("e"):
            clear_terminal()
            print("terminal cleared")
        time.sleep(0.1)  # Reduce CPU usage

def data_fetcher():
    while running:
        getPlaneInfo()
        time.sleep(3)

# Start threads
threading.Thread(target=keyboard_listener, daemon=True).start()
data_fetcher()  # Run in main thread so it blocks until done
