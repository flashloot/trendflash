import os
from google import genai

# 使用新版 SDK 初始化
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 災情內容
reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情"

# 使用 gemini-2.0-flash 或 gemini-1.5-flash
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
)

# 寫入檔案
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n\n{response.text}\n")

print("更新完成！")
