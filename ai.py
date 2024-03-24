import openai
# import config
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

openai.api_key = api_key

messages = [{"role": "system", "content": "Your job is to summarize text extracted from applicant resumes and provide resume reviewers accurate, comprehensive summaries about the applicants. Don't reply to this first message."}]

def AI(input):
    messages.append({"role": "user", "content": "You are being provided the text from an applicant's resume. Give me a three line summary of the applicant: " + input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    AI_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": AI_reply})
    return AI_reply
