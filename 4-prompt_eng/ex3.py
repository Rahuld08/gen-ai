from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question):
    SYSTEM_PROMPT="""
                    You are an English Grammar Expert.
                    You take incorrect sentences and return improved versions.
                    You do not explain the rule unless asked.
                    Example:
                    User: He go school
                    Assistant: He goes to school
                   
                  """
    response=client.responses.create(
        model="gpt-5.1",
        input=[
                {"role":"system","content":SYSTEM_PROMPT},
                {"role":"user","content":question}
            ],
        )
    print("Corrected:",response.output_text)
    
try:
    client=get_open_ai_client()
    print("Welcome To English Grammar Class")
    print("Type your sentence and to quit type exit")
    while True:
        sentence=input("Enter a sentence:")
        if sentence.lower()=="exit":
            break
        chat_with_ai(sentence)
except Exception as ex:
    print("Error:",ex)