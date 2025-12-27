import os
from google import genai
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# 2. Configure the Gemini API
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env file.")
    print("Please create a .env file based on .env.example and add your API key.")
    exit(1)

client = genai.Client(api_key=api_key)

def test_gemini():
    print("🚀 Testing Gemini AI (using google-genai)...")
    
    try:
        # Test prompt
        prompt = "Explain why 'The Matrix' (1999) is a cult classic in two sentences."
        
        print(f"User: {prompt}")
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt
        )
        
        print("\nGemini Response:")
        print("-" * 20)
        print(response.text)
        print("-" * 20)
        print("\n✅ Gemini AI integration working correctly!")
        
    except Exception as e:
        print(f"❌ Failed to test Gemini: {e}")

if __name__ == "__main__":
    test_gemini()
