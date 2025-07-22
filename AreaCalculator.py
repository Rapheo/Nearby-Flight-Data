import math

def calculate_bounds(lat, lon, distance_km=250):
    """
    Calculate bounding box for a square area of distance_km radius from center.
    Returns: (lamin, lamax, lomin, lomax)
    """
    lat_rad = math.radians(lat)

    delta_lat = distance_km / 111  # ~111 km per degree of latitude
    delta_lon = distance_km / (111 * math.cos(lat_rad))  # varies with latitude

    lamin = lat - delta_lat
    lamax = lat + delta_lat
    lomin = lon - delta_lon
    lomax = lon + delta_lon

    return round(lamin, 6), round(lamax, 6), round(lomin, 6), round(lomax, 6)

if __name__ == "__main__":
    lat = 23.7993984
    lon = 90.423296
    lamin, lamax, lomin, lomax = calculate_bounds(lat, lon, distance_km=250)

    print("lamin:", lamin)
    print("lamax:", lamax)
    print("lomin:", lomin)
    print("lomax:", lomax)

    url = (
        f"https://opensky-network.org/api/states/all"
        f"?lamin={lamin}&lamax={lamax}&lomin={lomin}&lomax={lomax}"
    )
    print("API URL:", url)
