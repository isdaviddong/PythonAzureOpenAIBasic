import os
import time
from openai import AzureOpenAI

def main():
    print("Ready...")
    
    # 初始化 Azure OpenAI 客戶端
    client = AzureOpenAI(
        azure_endpoint="https://_____________.openai.azure.com",
        api_key="___________________",
        api_version="2024-08-01-preview"
    )
    
    # 準備對話訊息
    messages = [
        {"role": "system", "content": "你是一個智能助理，你會回答任何問題，像是一個聰明的智者。"},
        {"role": "user", "content": "你能幫助我嗎?"},
        {"role": "assistant", "content": "好的，沒有問題。您請發問，我會盡力回答~"},
        {"role": "user", "content": "我該如何才能升官發財呢?"}
    ]
    
    # 使用串流方式取得回應
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=3000,
        stream=True
    )
    
    print("Assistant: ", end="", flush=True)
    
    # 逐字輸出串流回應
    for chunk in response:
        if chunk.choices and len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                # 逐字輸出
                for char in delta.content:
                    print(char, end="", flush=True)
                    time.sleep(0.01)  # 每個字元之間延遲 10 毫秒
    
    print()

if __name__ == "__main__":
    main()

