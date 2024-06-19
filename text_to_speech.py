import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play

from dotenv import load_dotenv


load_dotenv()

client = ElevenLabs(
  api_key=os.getenv("ELEVEN_API_KEY") 
)

def speak_text (chatbot_response):

  audio = client.generate(
  text=chatbot_response,
  voice="lFjzhZHq0NwTRiu2GQxy",
  model="eleven_multilingual_v2"
  )

  play(audio)

if __name__ == "__main__":
    # For standalone testing
    text_to_speak = "Halo, nama saya Steve"
    speak_text(text_to_speak)