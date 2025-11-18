import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENROUTER_API_KEY')
print(f"API Key: {api_key[:20]}..." if api_key else "No API key!")

try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=50
    )
    
    print("✅ SUCCESS! API key works!")
    print(f"Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ ERROR: {e}")