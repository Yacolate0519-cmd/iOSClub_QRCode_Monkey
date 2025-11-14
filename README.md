# 第 9 屆 iOS Club QRCode 快速產生器

這是一個簡單易用的 QR Code 生成工具，專為 iOS Club 社團設計。使用 QRCode Monkey API 生成帶有 iOS Club Logo 和自訂樣式的 QR Code。

## 功能特色

- 快速生成高品質 QR Code (1000x1000 像素)
- **🆕 自動縮短網址**：使用 TinyURL API 自動將長網址縮短，讓 QR Code 更簡潔美觀
- 內建 iOS Club Logo 作為中央圖示
- 獨特的圓形斑馬紋圖案設計
- 橘藍漸層配色 (#FFAF73 → #6D9DF8)
- 自動儲存至 ~/Downloads 資料夾

## 環境需求

- Python 3.12 或以上版本
- Conda (推薦使用 Miniforge)

## 安裝步驟

### 1. 使用 Conda 建立虛擬環境

```bash
# 使用 environment.yml 建立環境
conda env create -f environment.yml

# 啟動環境
conda activate qrcode_monkey
```

### 2. 手動安裝依賴（替代方案）

如果不使用 conda，也可以直接用 pip 安裝：

```bash
pip install requests==2.32.4
```

## 使用方法

1. 啟動 conda 環境：

```bash
conda activate qrcode_monkey
```

2. 執行程式：

```bash
python main.py
```

3. 輸入要轉換成 QR Code 的 URL：

```
Input the URL: https://your-url-here.com
🔄 正在縮短網址...
✅ 縮短後的網址: https://tinyurl.com/xxxxx
```

> **注意**：程式會自動嘗試縮短網址。如果 TinyURL API 發生錯誤，會自動使用原始網址並顯示警告訊息。

4. 等待生成完成，QR Code 會自動儲存至 `~/Downloads/qrcode.png`

## 專案結構

```
QRCode_Monkey/
├── main.py            # 主程式
├── environment.yml    # Conda 環境配置檔
├── final.jpg         # iOS Club Logo
└── README.md         # 說明文件
```

## 依賴套件

- **requests** (2.32.4) - 用於 HTTP API 請求

## 技術細節

### QR Code 樣式設定

- **圖案樣式**: 圓形斑馬紋 (circle-zebra)
- **眼睛樣式**: Frame1
- **漸層色彩**: #FFAF73 (橘) → #6D9DF8 (藍)
- **背景色彩**: 白色 (#FFFFFF)
- **Logo 模式**: Clean (乾淨模式)
- **輸出格式**: PNG
- **解析度**: 1000x1000 像素

### API 資訊

使用 [QRCode Monkey](https://www.qrcode-monkey.com/) 提供的免費 API：

```
https://api.qrcode-monkey.com/qr/custom
```

## 常見問題

### Q: 生成失敗怎麼辦？

A: 請檢查：

- 網路連線是否正常
- 輸入的 URL 格式是否正確
- API 服務是否正常運作

### Q: 可以修改 QR Code 樣式嗎？

A: 可以！在 `main.py` 中修改 `payload` 的 `config` 部分，調整顏色、圖案等設定。

### Q: 儲存位置可以更改嗎？

A: 可以修改 `main.py` 第 28 行的 `save_dir` 變數來改變儲存位置。

### Q: 如果短網址 API 失敗會怎樣？

A: 程式會自動偵測 API 錯誤，並使用原始網址繼續生成 QR Code，同時顯示警告訊息提醒你。

## 開發者資訊

- **社團**: 第 9 屆 iOS Club
- **開發者**: Yacolate0519-cmd
- **GitHub**: https://github.com/Yacolate0519-cmd/iOSClub_QRCode_Monkey

## 更新日誌

### v1.1.0

- 新增自動縮短網址功能（使用 TinyURL API）
- 預設啟用網址縮短，無需手動選擇
- API 錯誤時自動降級使用原始網址
- 改善使用者體驗，提供清楚的狀態提示
- 更新文件說明

### v1.0.0

- 初始版本發布
- 實作基本 QR Code 生成功能
- 整合 iOS Club Logo
- 自動儲存至 Downloads 資料夾
