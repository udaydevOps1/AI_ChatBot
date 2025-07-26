# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple rule-based response logic
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How can I assist you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day."
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines."
    else:
        return "I'm sorry, I don't understand that yet. Can you rephrase?"

# API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    reply = get_response(message)
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
