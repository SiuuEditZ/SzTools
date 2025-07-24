import requests
from utils.color import *

def run():
    domain = input("🔍 Masukkan domain: ").strip()
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        res = requests.get(url).json()
        subdomains = sorted(set([entry['name_value'] for entry in res]))
        for sub in subdomains:
            print_success(f"🌐 {sub}")
    except Exception as e:
        print_error(f"Gagal cari subdomain: {e}")
