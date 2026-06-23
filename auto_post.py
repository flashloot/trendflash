import os
from google import genai

# 初始化客戶端
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 這裡我們使用 'gemini-2.0-flash'
# 這是目前 Google 推薦且預設支援 generateContent 的模型名稱
model_name = "gemini-2.0-flash"

print(f"嘗試使用模型: {model_name}")

reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情"

# 執行生成
response = client.models.generate_content(
    model=model_name,
    contents=f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
)

# 寫入檔案
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n\n{response.text}\n")

print("更新完成！")
