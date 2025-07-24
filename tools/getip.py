import requests
from utils.color import *

def run():
    print(cyan("\n🌍 Get Public IP Tool"))
    print(yellow("🔍 Mengambil IP publik dari server..."))

    try:
        res = requests.get("https://api64.ipify.org?format=json")
        ip = res.json()["ip"]
        print(green(f"✅ IP Publik kamu: {ip} 🌐"))
    except Exception as e:
        print(red(f"❌ Gagal mengambil IP: {e}"))
