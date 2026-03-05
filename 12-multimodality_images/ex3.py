from openai import OpenAI
from dotenv import load_dotenv
import base64
import os
from datetime import datetime

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def refine_prompt(text_prompt):
    refine=client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
                Improve this into a detailed image prompt but not more than 50 words.
                {text_prompt}""")
    print(refine.output_text)
    return refine.output_text

def generate_image(refined_prompt,image_count):
    result=client.images.generate(
    model="gpt-image-1",
    prompt=refined_prompt,
    size="1024x1024",
    n=image_count)   
    image_id=datetime.now().strftime("%Y%m%d_%H%M%S")
    for i,img in enumerate(result.data):
        img_b64=img.b64_json
        image_bytes=base64.b64decode(img_b64)
        with open(f"generated/{image_id}_{i}.png","wb")as f:
            f.write(image_bytes)
        print(f"Saved to generated/{image_id}_{i}.png")

client=get_open_ai_client()
os.makedirs("generated",exist_ok=True)
while True:
    text_prompt=input("Enter image desc:").strip()
    if text_prompt.lower()=="exit":
        break
    image_count=int(input("Enter number of images you want:"))
    refined_prompt=refine_prompt(text_prompt)
    generate_image(refined_prompt,image_count)