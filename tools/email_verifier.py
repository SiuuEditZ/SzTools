import dns.resolver
from utils.color import *

def run():
    email = input("📧 Masukkan email: ")
    try:
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        if records:
            print_success(f"✅ Email domain aktif: {domain}")
    except Exception as e:
        print_error(f"❌ Email gak valid / domain mati: {e}")
