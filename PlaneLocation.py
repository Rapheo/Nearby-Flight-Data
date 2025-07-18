import requests
import keyboard

lat, lon = 23.7993984, 90.423296
delta = 0.027   # approx 3km or 3000 meter

url = (
    f"https://opensky-network.org/api/states/all"
    # f"?lamin={lat}&lomin={lon}"
    # f"&lamax={lat}&lomax={lon}"
    f"?lamin={lat-delta}&lomin={lon-delta}"
    f"&lamax={lat+delta}&lomax={lon+delta}"
)
r = requests.get(url)
data = r.json()

while True:
    if keyboard.is_pressed("q"):
        print("q pressed, ending loop")
        break
    
    if not data.get("states"):
        print("No airborne flights within ~3 km.")
    else:
        print("Flights overhead:")
        print(data["states"])
        for s in data["states"]:
            print(f"- Callsign: {s[1] or 'N/A'}, Position: ({s[6]:.4f}, {s[5]:.4f}), "
                f"Alt: {s[7]} m, Speed: {s[9]:.1f} m/s")
            

