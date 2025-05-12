# HealthHabit MVP Agent using Streamlit, Gemini API (via google.generativeai), and GitHub for version control

import streamlit as st
import os
import google.generativeai as genai

# --- Setup ---
st.title("🤖 HealthHabit AI – Your Personalized Micro-Habit Coach")

# Gemini API Key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

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
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating habit suggestion: {e}"

# --- Show Habit Suggestion ---
if st.button("Generate My Habit for Today"):
    with st.spinner("Thinking like your wellness coach..."):
        suggestion = generate_habit_recommendation()
        st.success("Here’s your habit for today:")
        st.write(suggestion)

# --- Footer ---
st.markdown("---")
st.caption("Powered by Gemini Pro API | MVP by HealthHabit.ai")
