from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def convert_text_to_audio(text_input):
    response=client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="marin",
    input=text_input)
    
    audio_bytes=response.read()
    audio_file=datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"audio/{audio_file}.mp3","wb")as f:
        f.write(audio_bytes)
    
    print(f"Audio saved as audio/{audio_file}.mp3")


client=get_open_ai_client()
os.makedirs("audio",exist_ok=True)
while True:
    text_input=input("Enter text:")
    if text_input.lower()=="exit":
        break
    convert_text_to_audio(text_input)