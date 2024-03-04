import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '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'

def chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.1,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
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

