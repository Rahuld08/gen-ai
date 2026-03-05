from google import genai
from dotenv import load_dotenv
from os import getenv

load_dotenv()
my_api_key=getenv("GEMINI_API_KEY")
if my_api_key is None:
    print("API Key not found!")
else:
    client=genai.Client(api_key=my_api_key)
    response=client.models.generate_content(model="gemini-2.5-flash",contents="Who is the Prime Minister Of India ? ?")
    print(response.text)