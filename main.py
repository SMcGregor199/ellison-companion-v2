ellison_message = "The light is the truth."
activities = ["reading", "writing", "coding", "listening to music"]
import requests
response = requests.get("https://bored-api.appbrewery.com/random")
import os
from openai import OpenAI

from dotenv import load_dotenv


load_dotenv()  # This reads the .env file
print("API Key Loaded:", os.getenv("OPENAI_API_KEY"))
"""
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make the request
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a wise literary scholar."},
        {"role": "user", "content": "What does Ralph Ellison say about invisibility?"}
    ]
)

# Print the reply
print(response.choices[0].message.content)
"""
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