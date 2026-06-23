import os
from google import genai

# 1. 初始化客戶端
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. 獲取所有可用的模型並選取一個
print("正在搜尋可用模型...")
models = list(client.models.list())
# 篩選出支援 generateContent 的模型
suitable_models = [m for m in models if "generateContent" in m.supported_methods]

if not suitable_models:
    print("錯誤：找不到任何支援的 AI 模型")
    exit(1)

# 選用第一個模型
target_model = suitable_models[0].name
print(f"自動偵測到可用模型: {target_model}")

# 3. 使用該模型執行任務
reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情"
response = client.models.generate_content(
    model=target_model,
    contents=f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
)

# 4. 寫入檔案
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n\n{response.text}\n")

print("更新完成！")
