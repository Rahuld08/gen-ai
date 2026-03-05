from openai import OpenAI
from dotenv import load_dotenv
import os
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

def chat_with_ai(transcribed_text,user_question):
    response=client.responses.create(model="gpt-4o-mini",input=[
        {
            "role":"user",
            "content":f"""
                        Here is transcribed text {transcribed_text}.
                        User question:
                        {user_question}
                        """
        }
    ])
    return response.output_text
 
#continue
client=get_open_ai_client()
audio_path=input("Enter audio file path:")
if not os.path.exists(audio_path):
    print("Audio file not found!")
else:
    transcribed_text=transcribe_audio(audio_path)
    while True:
        user_question=input("Type your question( To quit type exit)")
        if user_question.lower()=="exit":
            break
        answer=chat_with_ai(transcribed_text,user_question)
        print("\n🤖 AI Response:")
        print(answer)
    
