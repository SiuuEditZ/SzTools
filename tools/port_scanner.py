import socket
from utils.color import *

def run():
    host = input("📍 Masukkan host/IP: ").strip()
    try:
        for port in [21, 22, 80, 443, 8080]:
            s = socket.socket()
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print_success(f"🟢 Port {port} terbuka")
            else:
                print_warning(f"🔴 Port {port} tertutup")
            s.close()
    except Exception as e:
        print_error(f"Port scan error: {e}")
