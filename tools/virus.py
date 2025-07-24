import requests
from colorama import Fore, Style
import time

def run():
    print(Fore.CYAN + "\n🔍 VirusTotal Web Scanner")
    print(Fore.YELLOW + "⚠️  Gunakan untuk URL publik yang valid!" + Style.RESET_ALL)
    api_key = "YOUR_APIKEY"  

    url = input(Fore.GREEN + "\n🌐 Masukkan URL website: " + Style.RESET_ALL).strip()

    headers = {
        "x-apikey": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print(Fore.BLUE + "\n🚀 Mengirim permintaan ke VirusTotal..." + Style.RESET_ALL)
    response = requests.post(
        "https://www.virustotal.com/api/v3/urls",
        headers=headers,
        data=f"url={url}"
    )

    if response.status_code != 200:
        print(Fore.RED + f"❌ Gagal mengirim URL! ({response.status_code})" + Style.RESET_ALL)
        return

    url_id = response.json()["data"]["id"]
    time.sleep(2) 

    scan_result = requests.get(
        f"https://www.virustotal.com/api/v3/analyses/{url_id}",
        headers=headers
    ).json()

    print(Fore.MAGENTA + "\n📊 Hasil Analisis:" + Style.RESET_ALL)

    try:
        stats = scan_result["data"]["attributes"]["stats"]
        harmless = stats.get("harmless", 0)
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        undetected = stats.get("undetected", 0)
        timeout = stats.get("timeout", 0)

        print(Fore.GREEN + f"✅ Aman (Harmless): {harmless} 🔒")
        print(Fore.RED + f"💀 Berbahaya (Malicious): {malicious} ☠️")
        print(Fore.YELLOW + f"🤨 Mencurigakan (Suspicious): {suspicious} ❗")
        print(Fore.BLUE + f"🕵️ Tidak Terdeteksi (Undetected): {undetected} 🫥")
        print(Fore.CYAN + f"⌛ Timeout: {timeout} 💤" + Style.RESET_ALL)

        verdict = "🟢 Aman" if malicious == 0 and suspicious == 0 else "🔴 TERDETEKSI!"
        print(Fore.LIGHTMAGENTA_EX + f"\n📌 Verdict: {verdict}" + Style.RESET_ALL)

    except KeyError:
        print(Fore.RED + "❌ Gagal mendapatkan hasil scan!" + Style.RESET_ALL)
