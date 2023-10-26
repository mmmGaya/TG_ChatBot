import openai
import os
from dotenv import load_dotenv, find_dotenv
from prompt import context

load_dotenv(find_dotenv()) 

openai.api_key  = os.getenv('OPENAI_KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.3):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]

def collect_messages(prompt):
    context.append({'role':'user', 'content': prompt})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content': response})
    return response