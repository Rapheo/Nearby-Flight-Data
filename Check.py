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





#     def haversine(lat1, lon1, lat2, lon2):
#     R = 6371  # Earth radius in km
#     dlat = math.radians(lat2 - lat1)
#     dlon = math.radians(lon2 - lon1)
#     a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     return R * c

# def calculate_bearing(lat1, lon1, lat2, lon2):
#     # From point (lat2, lon2) to your location (lat1, lon1)
#     dlon = math.radians(lon1 - lon2)
#     lat1 = math.radians(lat1)
#     lat2 = math.radians(lat2)
#     x = math.sin(dlon) * math.cos(lat1)
#     y = math.cos(lat2) * math.sin(lat1) - math.sin(lat2) * math.cos(lat1) * math.cos(dlon)
#     bearing = math.degrees(math.atan2(x, y))
#     return (bearing + 360) % 360

# def is_heading_towards(plane_heading, bearing_to_you):
#     diff = abs(plane_heading - bearing_to_you)
#     return diff < 30 or diff > 330  # accounting for wrap-around

# def getPlaneInfo():
#     r = requests.get(url)
#     data = r.json()
#     count = 0
    
#     if not data.get("states"):
#         print(f"No airborne flights within ~{distance_km_val} km.")
#         return

#     results = []
#     for s in data["states"]:
#         try:
#             plane_lat = s[6]
#             plane_lon = s[5]
#             plane_heading = s[10]

#             if None in (plane_lat, plane_lon, plane_heading):
#                 continue

#             distance = haversine(lat, lon, plane_lat, plane_lon)
#             if distance > 25:
#                 continue

#             bearing = calculate_bearing(lat, lon, plane_lat, plane_lon)
#             if is_heading_towards(plane_heading, bearing):
#                 results.append({
#                     "callsign": s[1].strip() or "N/A",
#                     "position": (plane_lat, plane_lon),
#                     "altitude": s[7],
#                     "speed": s[9],
#                     "distance_km": round(distance, 2),
#                     "heading": plane_heading,
#                     "bearing_to_you": round(bearing, 1)
#                 })
#         except Exception as e:
#             continue

#     clear_terminal()
#     if results:
#         print("Flights within 25 km heading toward your location:\n")
#         for flight in results:
#             print(f"- Callsign: {flight['callsign']}, "
#                   f"Dist: {flight['distance_km']} km, "
#                   f"Pos: ({flight['position'][0]:.4f}, {flight['position'][1]:.4f}), "
#                   f"Alt: {flight['altitude']} m, "
#                   f"Speed: {flight['speed']:.1f} m/s, "
#                   f"Heading: {flight['heading']}°, "
#                   f"BearingToYou: {flight['bearing_to_you']}°")
#     else:
#         print("No flights within 25 km heading toward your location.")


