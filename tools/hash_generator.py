import hashlib
from utils.color import *

def run():
    text = input("📝 Masukkan teks: ")
    for algo in ['md5', 'sha1', 'sha256']:
        h = hashlib.new(algo)
        h.update(text.encode())
        print_success(f"{algo.upper()} 🔐: {h.hexdigest()}")
