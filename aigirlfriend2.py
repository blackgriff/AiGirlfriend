import langchain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3

openai_api_key="sksfK5micpYvl8IWtkRqi3T3BlbkFJ6FgjGnCPlKkdsh3fpnJ4"
# Load the OpenAI model using your API key
llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
conversation = ConversationChain(llm=llm)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']   
    response = conversation.run(user_message)
    return jsonify({'response': response})
