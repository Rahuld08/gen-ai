from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def create_prompt(topic):
    return [
        {
            "role":"system","content":"You are a Python tutor"
        },
        {
            "role":"user","content":f"Explain Python {topic} in 3 bullet points with just one example"
        }
    ]

def chat_with_ai(prompt):
    response=client.responses.create(
        model="gpt-5.1",
        input=prompt,
        )
    print("AI:",response.output_text)
    
try:
    client=get_open_ai_client()
    topic=input("Topic:")
    prompt=create_prompt(topic)
    chat_with_ai(prompt)
except Exception as ex:
    print("Error:",ex)