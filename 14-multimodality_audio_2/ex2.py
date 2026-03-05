from openai import OpenAI
from dotenv import load_dotenv
import os

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

client=get_open_ai_client()
response=client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="marin",
    input="Hello everyone, Welcome To The Generative AI class")

os.makedirs("audio",exist_ok=True)
audio_bytes=response.read()
with open("audio/output.mp3","wb")as f:
    f.write(audio_bytes)
print("Audio saved as audio/output.mp3")