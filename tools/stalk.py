import requests
import time

def run():
    print("\n🎯 Pilih platform untuk stalk:")
    print("1. TikTok")
    print("2. Instagram")
    platform = input("🔍 Pilihan (1/2): ").strip()

    if platform == "1":
        username = input("🎵 Masukkan username TikTok: @").replace("@", "")
        url = f"https://api.siputzx.my.id/api/stalk/tiktok?username={username}"
        stalk_tiktok(url)
    elif platform == "2":
        username = input("📸 Masukkan username Instagram: @").replace("@", "")
        url = f"https://api.siputzx.my.id/api/stalk/instagram?username={username}"
        stalk_instagram(url)
    else:
        print("❌ Pilihan tidak valid.")

def stalk_tiktok(api_url):
    print("\n⏳ Mengambil data TikTok...")
    try:
        res = requests.get(api_url).json()
        if res.get("status") and "data" in res:
            user = res["data"]["user"]
            stats = res["data"]["stats"]
            print(f"\n👤 Username: @{user['uniqueId']}")
            print(f"📛 Nama: {user['nickname']}")
            print(f"📝 Bio: {user['signature']}")
            print(f"🔗 Avatar: {user['avatarLarger']}")
            print(f"📈 Followers: {stats['followerCount']}")
            print(f"👥 Following: {stats['followingCount']}")
            print(f"❤️ Likes: {stats['heart']}")
            print(f"🎥 Video: {stats['videoCount']}")
        else:
            print("⚠️ Gagal mengambil data.")
    except Exception as e:
        print(f"❌ Error: {e}")

def stalk_instagram(api_url):
    print("\n⏳ Mengambil data Instagram...")
    try:
        res = requests.get(api_url).json()
        if res.get("status") and "data" in res:
            data = res["data"]
            print(f"\n👤 Username: @{data['username']}")
            print(f"📛 Nama: {data['full_name']}")
            print(f"📝 Bio: {data['biography']}")
            print(f"🔗 Avatar: {data['profile_pic_url']}")
            print(f"📈 Followers: {data['followers_count']}")
            print(f"👥 Following: {data['following_count']}")
            print(f"📸 Postingan: {data['posts_count']}")
        else:
            print("⚠️ Gagal mengambil data.")
    except Exception as e:
        print(f"❌ Error: {e}")
