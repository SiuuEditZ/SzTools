from colorama import Fore, Style
import os

def banner():
    print(Fore.CYAN + """\
░██████╗███████╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔════╝╚════██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
╚█████╗░░░███╔═╝░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
░╚═══██╗██╔══╝░░░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██████╔╝███████╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
""" + Style.RESET_ALL)

def menu():
    print(Fore.YELLOW + """\
1. IP Tracker 📍
2. WHOIS Lookup 🌐
3. Subdomain Finder 🧩
4. Base64 Encode/Decode 🔐
5. Hash Generator 🔒
6. Port Scanner 🚪
7. JSON Formatter 📦
8. Ping Tool 📡
9. Get Public IP 🌍
10. DNS Lookup 🧭
11. Email Verifier 📧
12. GeoIP Map 🗺️
13. Get IP from Domain 🔎
14. DDoS 💥
15. WAF Checker 🧱
16. 🔓 Leak Checker
17. Virus Scanner 🦠
18. Stalk Checker (IG & TikTok) 🔍
0. Exit 🚪
""" + Style.RESET_ALL)

def run_tool(choice):
    match choice:
        case "1": import tools.ip_tracker as tool; tool.run()
        case "2": import tools.whois_lookup as tool; tool.run()
        case "3": import tools.subdomain_finder as tool; tool.run()
        case "4": import tools.base64_tool as tool; tool.run()
        case "5": import tools.hash_generator as tool; tool.run()
        case "6": import tools.port_scanner as tool; tool.run()
        case "7": import tools.json_formatter as tool; tool.run()
        case "8": import tools.ping_tool as tool; tool.run()
        case "9": import tools.getip as tool; tool.run()
        case "10": import tools.dns_lookup as tool; tool.run()
        case "11": import tools.email_verifier as tool; tool.run()
        case "12": import tools.geoip_map as tool; tool.run()
        case "13": import tools.ipdomain as tool; tool.run()
        case "14": import tools.ddos as tool; tool.run()
        case "15": import tools.wafcheck as tool; tool.run()
        case "16": import tools.leak as tool; tool.run()
        case "17": import tools.virus as tool; tool.run()
        case "18": import tools.stalk as tool; tool.run()
        case "0": 
            print(Fore.GREEN + "👋 Byee!" + Style.RESET_ALL)
            exit()
        case _: 
            print(Fore.RED + "❌ Pilihan tidak valid, coba lagi yaa!" + Style.RESET_ALL)

if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        banner()
        menu()
        pilih = input(Fore.GREEN + "💬 Pilih menu: " + Style.RESET_ALL)
        run_tool(pilih)
        input(Fore.MAGENTA + "\n🔁 Tekan Enter untuk kembali ke menu..." + Style.RESET_ALL)
