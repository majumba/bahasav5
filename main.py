from speech_to_text import transcribe_speech
from chatbot import get_chatbot_response
from text_to_speech import speak_text

def main():
    # Step 1: Capture speech and transcribe it
    transcription = transcribe_speech()
    print(f"Transcription: {transcription}")

    # Step 2: Use the transcription as input to the chatbot
    chatbot_response = get_chatbot_response(transcription)
    print(f"Chatbot Response: {chatbot_response}")

    # Step 3: Convert the chatbot's response to speech
    speak_text(chatbot_response)

if __name__ == "__main__":
    main()



