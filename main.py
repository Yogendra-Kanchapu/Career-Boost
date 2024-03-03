from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/career_advice', methods=['POST'])
def career_advice():
    user_query = request.json.get('query')
    response = chatgpt_response(user_query)
    return jsonify({"response": response})

@app.route('/resume_feedback', methods=['POST'])
def resume_feedback():
    resume_text = request.json.get('resume')
    feedback = chatgpt_response("Provide feedback on this resume: " + resume_text)
    return jsonify({"feedback": feedback})

@app.route('/interview_tips', methods=['POST'])
def interview_tips():
    role = request.json.get('role')
    tips = chatgpt_response(f"Give interview preparation tips for a {role} position.")
    return jsonify({"tips": tips})

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

if __name__ == '__main__':
    app.run(debug=True)
