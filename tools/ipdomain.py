import socket
from utils.color import *

def run():
    print(cyan("\n🔎 Get IP from Domain"))
    domain = input(yellow("🌐 Masukkan domain (contoh: google.com): ")).strip()

    try:
        ip = socket.gethostbyname(domain)
        print(green(f"✅ IP untuk {domain} adalah: {ip} 🌍"))
    except socket.gaierror:
        print(red(f"❌ Gagal menemukan IP dari domain '{domain}'"))
