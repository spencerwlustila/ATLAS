import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


#connect to gemini
client = genai.Client(api_key = API_KEY)


# ATLAS CONVERSATION LOOP

print("ATLAS IS ONLINE...\n")

conversation = []

user_message = input("You: ")

while user_message.lower().strip() != "shutdown":
    # Store the user's message
    user_entry = {
        "role": "user",
        "parts": [{"text": user_message}]
    }

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

        # Display ATLAS's response
        print("\nATLAS:", response.text, "\n")

    except Exception:
        conversation.pop()
        
        print("ATLAS: Something went wrong. Please try again.")

    # Get the next message
    user_message = input("You: ")

print("ATLAS IS SHUTTING DOWN...")