from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def translate_audio(audio_path):
    with open(audio_path,"rb") as audio_file:
        result=client.audio.translations.create(
            file=audio_file,
            model="whisper-1")
    return result.text
    
client=get_open_ai_client()
audio_path="audio/sample2.m4a"
translated_text=translate_audio(audio_path)
print("AI Response")
print(translated_text)