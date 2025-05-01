import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

reply = ask_ellison("What does Ellison say about Richard Wright?")
print(reply)



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