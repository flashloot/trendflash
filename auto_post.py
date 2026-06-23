import os
from google import genai
from google.genai import types

# 1. 初始化客戶端
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. 修改模型名稱：使用 'gemini-1.5-flash' 並且不帶任何多餘路徑
# 如果這個名稱依然報 404，請確認你的 Google AI Studio 權限是否包含此模型
model_name = "gemini-1.5-flash"

try:
    print(f"嘗試使用模型: {model_name}")
    response = client.models.generate_content(
        model=model_name,
        contents="請用繁體中文回覆：測試成功"
    )
    print("AI 回應測試:", response.text)
    
    # 3. 執行正式任務
    reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情"
    final_response = client.models.generate_content(
        model=model_name,
        contents=f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
    )
    
    with open("index.html", "a", encoding="utf-8") as f:
        f.write(f"\n\n{final_response.text}\n")
    print("更新完成！")

except Exception as e:
    print(f"關鍵錯誤: {e}")
    # 列出所有可用的模型，幫助我們除錯
    print("正在嘗試列出所有可用模型...")
    for m in client.models.list():
        print(f"可用模型: {m.name}")
    raise e
