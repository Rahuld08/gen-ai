from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question):
    SYSTEM_PROMPT="""
                    You are an AI expert in coding.
                    You ony know Python and nothing else.
                    You help others in solving their Python doubts only.
                    If a user asks something apart from Python , then brutally roast them.
                  """
    response=client.responses.create(
        model="gpt-5.1",
        input=[
                {"role":"system","content":SYSTEM_PROMPT},
                {"role":"user","content":question}
            ],
        )
    print("AI:",response.output_text)
    
try:
    client=get_open_ai_client()
    question=input("Topic:")
    chat_with_ai(question)
except Exception as ex:
    print("Error:",ex)