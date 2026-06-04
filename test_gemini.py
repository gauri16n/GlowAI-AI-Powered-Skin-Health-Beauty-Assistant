import os
from dotenv import load_dotenv
from google import genai

print("Loading environment variables...")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: Could not find GEMINI_API_KEY in your .env file!")
else:
    print("✅ API Key found! Connecting to Google Gemini...")
    
    # Initialize the new genai Client
    client = genai.Client(api_key=api_key)
    
    print("\n🔍 Checking which models your key has access to:")
    for m in client.models.list():
        print(f" - {m.name}")
        
    print("🤖 Thinking...")
    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents="Give me one short and fun Ayurvedic skincare tip!"
        )
        print("\n✨ Gemini Says ✨")
        print(response.text)
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔍 Let's check which models your key has access to:")
        for m in client.models.list():
            print(f" - {m.name}")