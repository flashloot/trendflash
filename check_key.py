import os
import urllib.request
import json

# 這是 Google Gemini API 的直接網址
api_key = os.environ["GEMINI_API_KEY"]
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

data = {
    "contents": [{"parts": [{"text": "請回覆：測試成功"}]}]
}
encoded_data = json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=encoded_data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print("連線成功！AI 回應：", result['candidates'][0]['content']['parts'][0]['text'])
except Exception as e:
    print("連線失敗，錯誤是：", e)
