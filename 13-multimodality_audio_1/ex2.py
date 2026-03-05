from openai import OpenAI
from dotenv import load_dotenv

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def transcribe_audio(audio_path):
    with open(audio_path,"rb") as audio_file:
        result=client.audio.transcriptions.create(
            file=audio_file,
            model="gpt-4o-transcribe")
    return result.text
    
client=get_open_ai_client()
audio_path="audio/sample2.m4a"
transcribed_text=transcribe_audio(audio_path)
print("AI Response")
print(transcribed_text)