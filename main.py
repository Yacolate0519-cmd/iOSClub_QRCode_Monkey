import requests
import os

def shorten_url(long_url):
    """使用 TinyURL API 縮短網址"""
    try:
        api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text, True
        else:
            return long_url, False
    except Exception as e:
        return long_url, False

# 輸入網址
original_url = input("Input the URL: ")

# 自動縮短網址
print("🔄 正在縮短網址...")
content, success = shorten_url(original_url)

if success:
    print(f"✅ 縮短後的網址: {content}")
else:
    print(f"⚠️  短網址 API 發生錯誤，使用原始網址: {content}")

save_dir = os.path.expanduser("~/Downloads")
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "qrcode.png")
url = "https://api.qrcode-monkey.com/qr/custom"
logo = 'https://raw.githubusercontent.com/Yacolate0519-cmd/iOSClub_QRCode_Monkey/c6ff5817c3d5dff6a6ddee3336db33b074ba83a6/final.jpg'

payload = {
    "data": content,
    "config": {
        "body": "circle-zebra",
        "eye": "frame1",
        "erf1": ["fh"],
        "erf3": ["fh", "fv"],
        "eyeBall": "ball0",
        "gradientColor1": "#FFAF73",
        "gradientColor2": "#6D9DF8",
        "gradientOnEyes": True,
        "bgColor": "#ffffff",
        "logo": logo,
        "logoMode": "clean"
    },
    "size": 1000,
    "download": False,
    "file": "png"
}

try:
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        if response.content.startswith(b"\x89PNG"):
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"✅ QR Code 已成功保存至 {save_path}")
        else:
            try:
                result = response.json()
                if "imageUrl" in result:
                    image_url = "https://api.qrcode-monkey.com" + result["imageUrl"]
                    img = requests.get(image_url)
                    if img.status_code == 200:
                        with open(save_path, "wb") as f:
                            f.write(img.content)
                        print(f"✅ QR Code 已成功保存至 {save_path}")
                    else:
                        print(f"❌ 圖片下載失敗: {img.status_code}")
                else:
                    print("❌ API 回應中沒有圖片 URL")
            except:
                print(f"❌ 無法解析回應: {response.text[:100]}")
    else:
        print(f"❌ API 請求失敗: {response.status_code}")
        
except Exception as e:
    print(f"❌ 發生錯誤: {e}")