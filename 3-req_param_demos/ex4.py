from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question,temp,tokens):
    response=client.responses.create(
        model="gpt-5.1",
        input=question,
        temperature=temp,
        max_output_tokens=tokens)
    print(response.output_text)
    
try:
    client=get_open_ai_client()
    question=input("Type your question:")
    chat_with_ai(question,1.0,50)
except Exception as ex:
    print("Error:",ex)