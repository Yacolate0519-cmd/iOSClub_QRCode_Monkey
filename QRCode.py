import requests

content = input("Input the URL: ")
url = "https://api.qrcode-monkey.com/qr/custom"
logo = 'https://raw.githubusercontent.com/Yacolate0519-cmd/iOSClub_QRCode_Monkey/b84b14b8bacd54f7cc71d2e944b44167dd561395/background.png'

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
        # 檢查是否直接收到圖片
        if response.content.startswith(b"\x89PNG"):
            with open("qrcode.png", "wb") as f:
                f.write(response.content)
            print("✅ QR Code 已成功保存為 qrcode.png")
        else:
            try:
                result = response.json()
                if "imageUrl" in result:
                    image_url = "https://api.qrcode-monkey.com" + result["imageUrl"]
                    img = requests.get(image_url)
                    if img.status_code == 200:
                        with open("qrcode.png", "wb") as f:
                            f.write(img.content)
                        print("✅ QR Code 已成功保存為 qrcode.png")
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