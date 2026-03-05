from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key=os.getenv("OPENAI_API_KEY")
if my_api_key is None:
    print("API Key not found!")
else:
    client=OpenAI(api_key=my_api_key)
    response=client.responses.create(
        model="gpt-5.1",
        input="What is the capital of India ?"
    )
    print(response.output_text)