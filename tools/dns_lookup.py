import dns.resolver
from utils.color import *

def run():
    domain = input("🌐 Masukkan domain: ")
    try:
        records = dns.resolver.resolve(domain, 'A')
        for r in records:
            print_success(f"📦 IP: {r}")
    except Exception as e:
        print_error(f"DNS error: {e}")
