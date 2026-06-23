import os
import google.generativeai as genai

# 使用正確的模型名稱路徑
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('models/gemini-1.5-flash')

reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情，許多玩家反映無法連線到 5G 頻段。"

# 請求 AI 生成內容
prompt = f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
response = model.generate_content(prompt)

# 將結果寫入 index.html
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n<!-- 自動新增災情 -->\n{response.text}\n")

print("更新完成！")
