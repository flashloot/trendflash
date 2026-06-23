import os
import google.generativeai as genai
import sys

# 檢查環境變數有沒有讀到
key = os.environ.get("GEMINI_API_KEY")
if not key:
    print("錯誤：找不到 GEMINI_API_KEY")
    sys.exit(1)

# 測試連線
try:
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("連線成功，模型載入中...")
    response = model.generate_content("Hello")
    print("AI 回應成功：" + response.text)
except Exception as e:
    print(f"發生錯誤: {e}")
    sys.exit(1)
