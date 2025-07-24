import requests
from utils.color import *

def run():
    ip = input("📍 Masukkan IP: ")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            lat, lon = res['lat'], res['lon']
            print_success(f"🗺️ Lokasi: https://www.google.com/maps?q={lat},{lon}")
        else:
            print_error("IP gak valid")
    except Exception as e:
        print_error(f"GeoIP error: {e}")
