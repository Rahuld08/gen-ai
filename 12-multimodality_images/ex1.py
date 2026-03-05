from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

client=get_open_ai_client()
result=client.images.generate(
    model="gpt-image-1",
    prompt="A cute baby with a cheerful smile",
    size="1024x1024",
    n=1)   

print(result)
img_64=result.data[0].b64_json 
img_bytes=base64.b64decode(img_64)
os.makedirs("generated",exist_ok=True)
with open("generated/baby.png","wb") as f:
    f.write(img_bytes)
print("Image saved!")