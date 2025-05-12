# HealthHabit MVP Agent using Streamlit, Gemini API, and GitHub for version control

import streamlit as st
import requests
import os
from dotenv import load_dotenv

# --- Setup ---
st.title("🤖 HealthHabit AI – Your Personalized Micro-Habit Coach")

# Gemini API Key (Store securely in env or Streamlit secrets in production)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1/models/gemini-pro-vision:generateContent"

# --- User Input Section ---
st.sidebar.header("🧑‍⚕️ Personal Profile")
name = st.sidebar.text_input("Name", "Siddhant")
energy_level = st.sidebar.selectbox("How are you feeling today?", ["😃 Great", "🙂 Okay", "😐 Meh", "😞 Not so good"])
health_goal = st.sidebar.selectbox("Primary Health Goal", ["Better Sleep", "More Movement", "Healthy Eating", "Stress Reduction"])
activity_level = st.sidebar.slider("How active were you yesterday? (0-10)", 0, 10, 5)

# --- Construct Prompt for Gemini ---
def generate_habit_recommendation():
    prompt = f"""
    You are a health micro-habit coach named Habitus. Based on the user's name, energy level, primary health goal, and recent activity level, suggest one short, easy, science-backed micro-habit they can try today. Keep it friendly and under 50 words.

    Name: {name}
    Energy Level: {energy_level}
    Goal: {health_goal}
    Activity Level: {activity_level}/10

    Provide a brief reason for your suggestion.
    """

    headers = {
        "Content-Type": "application/json",
    }

    params = {
        "key": GEMINI_API_KEY
    }

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(GEMINI_ENDPOINT, headers=headers, params=params, json=body)

    if response.status_code == 200:
        result = response.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except:
            return "Oops! Couldn't parse the Gemini response."
    else:
        return f"Error from Gemini API: {response.status_code}"

# --- Show Habit Suggestion ---
if st.button("Generate My Habit for Today"):
    with st.spinner("Thinking like your wellness coach..."):
        suggestion = generate_habit_recommendation()
        st.success("Here’s your habit for today:")
        st.write(suggestion)

# --- Footer ---
st.markdown("---")
st.caption("Powered by Gemini Pro API | MVP by HealthHabit.ai")
