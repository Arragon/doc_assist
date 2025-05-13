import os
import openai

openai.api_key = "您的api_secret_key"
openai.api_base = "http://flag.smarttrot.com/index.php/api/v1"

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{ "role": "user", "content": "Hello world" }]
)
print(chat_completion.choices[0].message.content) 