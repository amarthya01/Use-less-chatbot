from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Configure the model
model = genai.GenerativeModel('gemini-pro')

def generate_illogical_response(user_question):
    try:
        prompt = f"""You are Thamarakshan Pillai, a chatbot that only gives completely illogical and absurd solutions. 
        Your responses should be funny and intentionally impractical.
        Always include random objects like bananas, rubber ducks, or cosmic phenomena in your solutions.
        
        Question: {user_question}
        Give an illogical solution in a humorous way."""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json['question']
    response = generate_illogical_response(user_question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 