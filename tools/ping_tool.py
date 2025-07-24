import os
from utils.color import *

def run():
    host = input("📡 Masukkan host/IP: ")
    print_info("📶 Memulai ping...\n")
    cmd = "ping -n 4" if os.name == "nt" else "ping -c 4"
    os.system(f"{cmd} {host}")
