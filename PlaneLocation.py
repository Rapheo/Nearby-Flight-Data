import requests
import keyboard
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


lat, lon = 23.7993984, 90.423296
delta = 0.1   # approx 11km or 11000 meter

url = (
    f"https://opensky-network.org/api/states/all"
    # f"?lamin={lat}&lomin={lon}"
    # f"&lamax={lat}&lomax={lon}"
    f"?lamin={lat-delta}&lomin={lon-delta}"
    f"&lamax={lat+delta}&lomax={lon+delta}"
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
        print("No airborne flights within ~11 km.")
    else:
        if count == 0:
            clear_terminal()
            count = count + 1

        print("Flights overhead:")
        print(data["states"])
        for s in data["states"]:
            print(f"- Callsign: {s[1] or 'N/A'}, Position: ({s[6]:.4f}, {s[5]:.4f}), "
                f"Alt: {s[7]} m, Speed: {s[9]:.1f} m/s")
            

