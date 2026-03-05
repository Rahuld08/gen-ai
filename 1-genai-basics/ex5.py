from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client=OpenAI()
response=client.responses.create(
    model="gpt-5.1",
    input="What is the capital of India ?"
)
print(response.output_text)