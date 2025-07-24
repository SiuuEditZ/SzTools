import socket
import whois
from utils.color import *

def run():
    domain = input("🌐 Masukkan domain: ").strip()
    try:
        data = whois.whois(domain)
        print_success(f"🔐 Registrar: {data.registrar}")
        print_success(f"📆 Tanggal Buat: {data.creation_date}")
        print_success(f"🔁 Expired: {data.expiration_date}")
        print_success(f"👤 Name: {data.name}")
    except Exception as e:
        print_error(f"WHOIS gagal: {e}")
