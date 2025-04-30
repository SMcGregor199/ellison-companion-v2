ellison_message = "The light is the truth."
activities = ["reading", "writing", "coding", "listening to music"]
import requests
response = requests.get("https://bored-api.appbrewery.com/random")

from dotenv import load_dotenv
import os

load_dotenv()  # This reads the .env file
api_key = os.getenv("OPENAI_API_KEY")  # This grabs the value of that key

response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-4" if you have access gpt-3.5-turbo
    messages=[
        {"role": "system", "content": "You are a wise literary scholar."},
        {"role": "user", "content": "What does Ralph Ellison say about invisibility?"}
    ]
)

print("\nAI says:\n")
print(response["choices"][0]["message"]["content"])
"""
if response.status_code == 200:
    data = response.json()
    print("\nHere’s a suggestion from the Bored API:")
    print(f"- {data['activity']}")
else:
    print("Could not fetch activity. Try again later.")

for activity in activities:
    print(f"One thing I enjoy is {activity}.")



print(ellison_message)

"""