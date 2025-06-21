import streamlit as st
from app import get_groq_response

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