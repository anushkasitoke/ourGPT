import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_groq_response(quries):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": quries ,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content