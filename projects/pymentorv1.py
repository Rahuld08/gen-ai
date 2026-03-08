from openai import OpenAI
from dotenv import load_dotenv


def get_open_ai_client():
    load_dotenv()
    return OpenAI()


def chat_with_ai(question):
    response = client.responses.create(model="gpt-5.1", input=question)
    print("AI  :=>", response.output_text)


try:
    client = get_open_ai_client()
    while True:
        question = input("Your:=> ")
        if question.lower() == "exit":
            break
        chat_with_ai(question)
except Exception as ex:
    print("Error", ex)
