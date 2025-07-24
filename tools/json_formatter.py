import json
from utils.color import *

def run():
    teks = input("📥 Masukkan JSON: ")
    try:
        data = json.loads(teks)
        pretty = json.dumps(data, indent=4)
        print_success("🧾 JSON diformat:")
        print(pretty)
    except Exception as e:
        print_error(f"Bukan JSON valid: {e}")
