from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question):
    stream=client.responses.create(
        model="gpt-5.1",
        input=question,
        stream=True)
    for event in stream:
        if event.type=="response.output_text.delta":
            print(event.delta,end="")
    
try:
    client=get_open_ai_client()
    question=input("Type your question:")
    chat_with_ai(question)
except Exception as ex:
    print("Error:",ex)