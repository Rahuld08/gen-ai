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
    n=3)   

os.makedirs("generated",exist_ok=True)
for i,img in enumerate(result.data):
    img_b64=img.b64_json
    image_bytes=base64.b64decode(img_b64)
    with open(f"generated/baby{i}.png","wb") as f:
        f.write(image_bytes)
    print(f"Saved to generarted/baby{i}.png")