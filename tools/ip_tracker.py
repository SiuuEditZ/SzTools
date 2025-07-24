import requests
from utils.color import *

def run():
    ip = input("📡 Masukkan IP target: ").strip()
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            print_success(f"🌎 Negara: {res['country']}")
            print_success(f"🏙️ Kota: {res['city']}")
            print_success(f"🛰️ ISP: {res['isp']}")
            print_success(f"📍 Koordinat: {res['lat']}, {res['lon']}")
        else:
            print_error("IP tidak valid 😓")
    except Exception as e:
        print_error(f"Gagal ambil data: {e}")
