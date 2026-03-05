from openai import OpenAI
client = OpenAI(api_key="sk-proj-")
 
response=client.responses.create(model="gpt-5.1", input="Hello, I am Sachin. What about you?")

print(response.output_text)