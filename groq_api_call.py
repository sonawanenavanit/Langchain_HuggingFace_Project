import streamlit as st
import os
from groq import Groq

client = Groq(
    api_key='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',
)
query = st.text_input(" ")

if query:
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature = 0.5,
            # max_competion_tokens=10
        )

    st.write(chat_completion.choices[0].message.content) 