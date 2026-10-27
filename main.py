import os
from dotenv import load_dotenv
from google import genai

#calls from transcription and speaker
from voice.transcription import transcribe_audio
from voice.speaker import speak

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


#connect to gemini
client = genai.Client(api_key = API_KEY)


# ATLAS CONVERSATION LOOP

print("ATLAS IS ONLINE...\n")

conversation = []

user_message = transcribe_audio()

while user_message.lower().strip().strip("!?.").replace(" ", "") != "shutdown":
    if not user_message.strip():
        print("ATLAS: No speech detected.")
        user_message = transcribe_audio()
        continue

    # Store the user's message
    user_entry = {
        "role": "user",
        "parts": [{"text": user_message}]
    }

    conversation_saved = False

    try:
        conversation.append(user_entry)

    # Send conversation history to Gemini
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation
        )

    # Store ATLAS's response
        atlas_entry = {
            "role": "model",
            "parts": [{"text": response.text}]
        }

        conversation.append(atlas_entry)
        conversation_saved = True

        # Display ATLAS's response
        print("\nATLAS:", response.text, "\n")
        speak(response.text)

    except Exception:
        if conversation_saved == False:
            conversation.pop()

        print("ATLAS: Something went wrong. Please try again.")

    # Get the next message
    user_message = transcribe_audio()

print("ATLAS IS SHUTTING DOWN...")