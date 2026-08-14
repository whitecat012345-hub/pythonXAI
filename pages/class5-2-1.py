import openai # pip install openai
from dotenv import load_dotenv
import os
load_dotenv() # 讀取 .env 檔案
#設定api 金鑰
openai_api_key = os.getenv("OPENAI_API_KEY") 
while True:
    user_input = input("你:")
    if user_input.lower() == ['exit','quit']:
        break
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後續對話"},
            {"role": "user", "content": user_input}
        ],
    )
    assistant_message=response.choices[0].message.content
    print(f'AI:{assistant_message}')