from google import genai
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import get_key

# Simple example of using the GenAI client
# Using chat so AI can remember the context of the conversation

client = genai.Client(api_key=get_key())

# Create a chat
chat = client.chats.create(model='gemini-2.0-flash')
while True:
    question = input('[User]: ')
    # send message to chat to generate a response
    response = chat.send_message(message=question)
    print('[GenAI]:', response.text)

    if question.strip() == 'exit' or question.strip() == 'quit':
        break

# History of chat
for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)