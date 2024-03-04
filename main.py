import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv('OPENAI_API_KEY')
# Set your OpenAI API key here

from openai import OpenAI
client = OpenAI(api_key=api_key)

def chatgpt_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
    {"role": "system", "content": "You are a resume reviewer."},
    {"role": "user", "content": f"{prompt}"}
  ] 
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

st.title("Career and Internship Navigator")

with st.form(key='career_navigator'):
    user_input = st.text_area("Ask for career advice, get resume feedback, or interview tips:")
    submit_button = st.form_submit_button(label='Submit')

if submit_button and user_input:
    if "resume" in user_input.lower():
        feedback_prompt = "Provide feedback on this resume: " + user_input
        feedback = chatgpt_response(feedback_prompt)
        st.write(feedback)
    elif "interview" in user_input.lower():
        tips_prompt = f"Give interview preparation tips for a {user_input} position."
        tips = chatgpt_response(tips_prompt)
        st.write(tips)
    else:
        advice = chatgpt_response(user_input)
        st.write(advice)
