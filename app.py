import google.generativeai as genai
import os
import streamlit as st

# get api key from local environment
key = os.getenv("GOOGLE_API_KEY")

# configure the model
genai.configure(api_key=key)

# use a valid model (check available models with genai.list_models())
model = genai.GenerativeModel("gemini-1.5-flash")

# frontend UI
st.title("SIMPLE TEXT GENERATION")
st.header("This is to test the Gemini model as application")

# input box
prompt = st.text_input("Write your prompt", max_chars=10000)

# check if user entered something
if prompt:
    response = model.generate_content(prompt)
    st.write(response.text)
else:
    st.info("Please enter a prompt above to generate content.")