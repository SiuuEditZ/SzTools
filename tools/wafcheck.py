import requests
from utils.color import cyan, green, red

def run():
    print(cyan("\n🧱 WAF Detector"))
    url = input("🔗 Masukkan URL target: ").strip()

    try:
        headers = {"User-Agent": "WAF-Detector-Test"}
        response = requests.get(url, headers=headers, timeout=10)

        waf_headers = [
            "X-Sucuri-ID", "X-WAF", "Server", "X-CDN", "CF-RAY", "X-Akamai", "X-FireEye"
        ]
        detected = []

        for h in waf_headers:
            if h in response.headers:
                detected.append(f"{h}: {response.headers[h]}")

        if detected:
            print(green("✅ WAF terdeteksi!\n"))
            for d in detected:
                print("  🔍 " + d)
        else:
            print(red("❌ Tidak terdeteksi WAF yang umum."))

    except Exception as e:
        print(red(f"🚨 Error: {e}"))
