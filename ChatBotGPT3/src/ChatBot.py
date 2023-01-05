import os
import openai

class ChatBot:

    def __init__(self, api_key, name="chatbot", model="text-davinci-003", max_token=150):
        self.name = name
        self.model = model
        self.api_key = api_key
        self.max_token = max_token

    