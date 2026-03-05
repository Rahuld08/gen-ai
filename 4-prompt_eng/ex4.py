from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def chat_with_ai(question):
    SYSTEM_PROMPT="""
                    You are sentiment classifier.
                    You respond jut Positive or Negative based on the input.
                    
                    Example 1:
                    User: I love this movie.
                    Assistant: Positive
                    
                    Example 2:
                    User: This product is terrible.
                    Assistant: Negative
                    
                    Example 3:
                    User: Your service was amazing.
                    Assistant: Positive
                   
                  """
    response=client.responses.create(
        model="gpt-5.1",
        input=[
                {"role":"system","content":SYSTEM_PROMPT},
                {"role":"user","content":question}
            ],
        )
    print("Sentiment:",response.output_text)
    
try:
    client=get_open_ai_client()
    print("Welcome To Sentiment Classifier")
    print("Type your sentence and to quit type exit")
    while True:
        sentence=input("Enter a sentence:")
        if sentence.lower()=="exit":
            break
        chat_with_ai(sentence)
except Exception as ex:
    print("Error:",ex)