from google import genai
from dotenv import load_dotenv

def get_gemini_ai_client():
    load_dotenv()
    client=genai.Client()
    return client

def chat_with_ai():
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Who is the Prime Minister Of India ?"
    )
    print(response.text)

client=get_gemini_ai_client()
chat_with_ai()