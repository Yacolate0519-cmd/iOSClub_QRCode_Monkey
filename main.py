import requests
import os

original_url = input("Input the URL: ")
save_dir = os.path.expanduser("~/Downloads")
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "qrcode.png")
url = "https://api.qrcode-monkey.com/qr/custom"
logo = "https://raw.githubusercontent.com/Yacolate0519-cmd/iOSClub_QRCode_Monkey/8118921f4fd0aa10f208432e1c3ed067e56cac7c/final.jpg"

payload = {
    "data": original_url,
    "config": {
        "body": "circle",
        "eye": "frame13",
        "erf1": ["fh"],
        "erf3": ["fh", "fv"],
        "eyeBall": "ball15",
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