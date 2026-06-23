import os
import google.generativeai as genai

# 設定 AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 災情內容
reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情，許多玩家反映無法連線到 5G 頻段。"

# 請 AI 寫成 HTML
prompt = f"請將這條災情寫成一段適合網站的 HTML 卡片代碼 (包含標題、描述、解決建議)。新聞內容：{reddit_news}"
response = model.generate_content(prompt)

# 將生成的 HTML 寫入 index.html
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n<!-- 自動新增災情 -->\n{response.text}\n")

print("更新完成！")
