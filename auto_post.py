import os
import time
from google import genai
from google.genai import types

# 初始化客戶端
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def main():
    model_name = "gemini-2.0-flash"
    reddit_news = "Steam Deck OLED 版最近在更新後出現 Wi-Fi 斷連災情"
    
    # 簡單的重試機制，如果遇到配額問題，等待 60 秒後嘗試一次
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
        )
        
        with open("index.html", "a", encoding="utf-8") as f:
            f.write(f"\n\n{response.text}\n")
        print("更新完成！")
        
    except Exception as e:
        if "429" in str(e):
            print("遇到配額限制，正在等待 60 秒...")
            time.sleep(60)
            # 再試一次
            response = client.models.generate_content(
                model=model_name,
                contents=f"請將這條災情寫成一段適合網站的 HTML 卡片代碼。新聞內容：{reddit_news}"
            )
            with open("index.html", "a", encoding="utf-8") as f:
                f.write(f"\n\n{response.text}\n")
            print("重試後更新完成！")
        else:
            raise e

if __name__ == "__main__":
    main()
