 

import streamlit as st
import random
import json
import datetime

# Sample motivational quotes
quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Act as if what you do makes a difference. It does. – William James"
]

# Sample motivational videos
videos = [
    "https://www.youtube.com/watch?v=ZXsQAXx_ao0",
    "https://www.youtube.com/watch?v=mgmVOuLgFB0",
    "https://www.youtube.com/watch?v=wnHW6o8WMas",
]

# Sample daily challenges
challenges = [
    "Write down three things you are grateful for today.",
    "Take a 5-minute break and practice deep breathing.",
    "Read 5 pages of a self-improvement book.",
    "Reach out to a friend and share something positive.",
    "Write a short reflection on a recent challenge and what you learned from it."
]

# File to store user reflections
DATA_FILE = "user_reflections.json"

# Function to load user reflections
def load_reflections():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save user reflections
def save_reflection(reflection):
    reflections = load_reflections()
    reflections.append({"date": str(datetime.date.today()), "reflection": reflection})
    with open(DATA_FILE, "w") as file:
        json.dump(reflections, file, indent=4)

# Streamlit UI
st.set_page_config(page_title="Motivational Dashboard", layout="wide")

st.title("🌟 Motivational Dashboard")

# Display a random motivational quote
st.subheader("💡 Today's Motivation")
st.write(random.choice(quotes))

# Display a random motivational video
st.subheader("🎥 Watch & Get Inspired")
st.video(random.choice(videos))

# Display a daily challenge
st.subheader("🔥 Daily Challenge")
st.write(random.choice(challenges))

# User Reflection Input
st.subheader("📝 Share Your Thoughts")
reflection = st.text_area("What inspired you today?", "")
if st.button("Save Reflection"):
    if reflection:
        save_reflection(reflection)
        st.success("Your reflection has been saved!")
    else:
        st.warning("Please write something before saving.")

# Show past reflections
st.subheader("📜 Your Past Reflections")
past_reflections = load_reflections()
for ref in past_reflections[-5:]:  # Show only last 5 reflections
    st.write(f"📅 {ref['date']}: {ref['reflection']}")

st.write("💖 Stay positive and keep growing!")