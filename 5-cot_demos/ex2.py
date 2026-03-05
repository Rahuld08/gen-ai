from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question,system_prompt="You are a helpful assistant"):
    response=client.responses.create(
        model="gpt-4.1-mini",
        input=[
                    {
                        "role":"system","content":system_prompt
                    },
                    {
                        "role":"user","content":question}
              ],
        )
    return response.output_text

def simple_puzzle():
    question="A is taller than B, B is taller than C. Then who is shortest ?"
    response=chat_with_ai(question)
    print("Response:",response)

def simple_puzzle_with_cot():
    question="A is taller than B, B is taller than C. Then who is shortest ?"
    system_prompt="""
                   You are a helpful assistant.
                   Please explain the reasoning step by step before arrving to the result
                  """
    response=chat_with_ai(question,system_prompt)
    print("Response:",response)



    
try:
    client=get_open_ai_client()
    simple_puzzle_with_cot()
except Exception as ex:
    print("Error:",ex)