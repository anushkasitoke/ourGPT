# Streamlit app for Groq Chatbot (Llama-3.3-70b-versatile) - Single file deployable version
import os
import streamlit as st
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

st.title("Groq Chatbot (Llama-3.3-70b-versatile)")

user_query = st.text_area("Enter your query:")

if st.button("Submit"):
    if user_query.strip():
        with st.spinner("Getting response..."):
            response = get_groq_response(user_query)
        st.markdown("**Response:**")
        st.write(response)
    else:
        st.warning("Please enter a query.")
