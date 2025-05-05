from flask import Flask, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv
from parse_excerpts import load_excerpts
from flask_cors import CORS

excerpts = load_excerpts()
load_dotenv() 
app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def find_relevant_excerpts(prompt, excerpts, max_count=2):
    matches = []
    for excerpt in excerpts:
        if any(tag.lower() in prompt.lower() for tag in excerpt["tags"]):
            matches.append(excerpt)
        if len(matches) >= max_count:
            break
    return matches

def ask_ellison(prompt): 
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system","content":"You are a wise literary scholar."},
                {"role":"user","content":prompt}
            ]
        )
        print("AI Says:")
        return response.choices[0].message.content

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    matches = find_relevant_excerpts(prompt, excerpts)

    system_msg = "You are a literary assistant trained on the work of Ralph Ellison.\n"
    for m in matches:
        system_msg += f"\nExcerpt from '{m['title']}':\n{m['content']}\n"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg.strip()},
            {"role": "user", "content": prompt}
        ]
    )
    return jsonify({"answer": response.choices[0].message.content})


# reply = ask_ellison("What does Ellison say about Richard Wright?")
# print(reply)



"""
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a wise literary scholar."},
            {"role": "user", "content": "What does Ralph Ellison say about invisibility?"}
        ]
    )
    ## print("AI Says:")
    # Print the reply
    ## print(response.choices[0].message.content)

import requests
response = requests.get("https://bored-api.appbrewery.com/random")

if response.status_code == 200:
    data = response.json()
    print("\nHere’s a suggestion from the Bored API:")
    print(f"- {data['activity']}")
else:
    print("Could not fetch activity. Try again later.")

for activity in activities:
    print(f"One thing I enjoy is {activity}.")


    activities = ["reading", "writing", "coding", "listening to music"]

"""