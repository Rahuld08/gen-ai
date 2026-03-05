from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question,system_prompt="You are a maths teacher"):
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

def simple_math():
    question="How much is 459*245 ?"
    response=chat_with_ai(question)
    print("Response:",response)

def simple_math_with_cot():
    question="How much is 459*245 ?"
    system_prompt="""
                   You are a maths teacher.
                   Please explain the reasoning step by step before arrving to the result
                  """
    response=chat_with_ai(question,system_prompt)
    print("Response:",response)



    
try:
    client=get_open_ai_client()
    simple_math_with_cot()
except Exception as ex:
    print("Error:",ex)