import requests
from utils.color import cyan, green, red

def run():
    print(cyan("\n🔓 Leak Checker (Email/Username)"))
    query = input("🕵️ Masukkan email atau username: ").strip()

    try:
        url = f"https://leakcheck.io/api/public?check={query}"
        r = requests.get(url)
        if "leaked" in r.text or "found" in r.text.lower():
            print(green("💥 Terindikasi bocor di database publik!"))
        else:
            print(red("✅ Aman! Tidak ditemukan kebocoran."))
    except Exception as e:
        print(red(f"🚨 Gagal cek data: {e}"))
