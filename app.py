import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use a valid Gemini chat-compatible model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

# Start chat with memory
chat = model.start_chat(history=[])

def ask_gemini(prompt):
    response = chat.send_message(prompt)
    return response.text

if __name__ == "__main__":
    print("💬 Gemini 2.5 Pro AI Chat - Start chatting (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        try:
            reply = ask_gemini(user_input)
            print("Gemini:", reply)
        except Exception as e:
            print("⚠️ Error:", e)
