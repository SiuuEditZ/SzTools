import base64
from utils.color import *

def run():
    text = input("📥 Masukkan teks: ")
    action = input("🔁 Encode / Decode (e/d)? ").lower()
    try:
        if action == "e":
            hasil = base64.b64encode(text.encode()).decode()
            print_success(f"🔒 Encoded: {hasil}")
        elif action == "d":
            hasil = base64.b64decode(text).decode()
            print_success(f"🔓 Decoded: {hasil}")
        else:
            print_warning("Pilihan harus 'e' atau 'd'")
    except Exception as e:
        print_error(f"Error base64: {e}")
