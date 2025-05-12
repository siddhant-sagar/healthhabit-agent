# 🌱 HealthHabit AI – Personalized Micro-Habit Coach

**HealthHabit AI** is an MVP wellness assistant built with Streamlit and powered by Google's Gemini Pro. It provides friendly, science-backed, and context-aware micro-habit suggestions based on user mood, goals, and daily activity level.

---

## 🛠 Tech Stack

| Component   | Technology                  |
|-------------|-----------------------------|
| Frontend    | Streamlit                   |
| AI Backend  | Gemini Pro via `google.generativeai` |
| Deployment  | Streamlit Cloud             |
| Language    | Python                      |

---

## 🚀 Features

- ✅ Personalized micro-habit suggestions
- 🤖 Gemini Pro-powered recommendation engine
- 📊 Daily mood, goal, and activity input
- 📱 Lightweight, mobile-friendly Streamlit UI

---

## 🔧 Setup Instructions (Local & Cloud)

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/healthhabit-agent.git
cd healthhabit-agent
```

---

### ✅ Step 2: Create Environment & Install Dependencies

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install streamlit google-generativeai
```

---

### ✅ Step 3: Add Gemini API Key

Create a directory and file named `.streamlit/secrets.toml`:

```bash
mkdir .streamlit
nano .streamlit/secrets.toml
```

Paste the following:

```toml
GEMINI_API_KEY = "your_google_generative_ai_key_here"
```

---

### ✅ Step 4: Run the App Locally

```bash
streamlit run app.py
```

The app will be available at: `http://localhost:8501`

---

## 🌐 Deploy to Streamlit Cloud

1. Push your project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Create a new app and select your GitHub repo
4. Set the file path to `app.py`
5. In **App Settings → Secrets**, add:
   ```
   GEMINI_API_KEY = your_google_generative_ai_key_here
   ```
6. Click **Deploy** and you’re live! 🎉

---

## 📸 Example Screenshot

> ![image](https://github.com/user-attachments/assets/0bc7b75e-37fa-412f-b18b-90c5fae04ae8)


---

## 👥 Contributors

- **Siddhant Sagar** – [@ssagar2](mailto:ssagar2@andrew.cmu.edu)
- **Gemini AI** – Powered by Google Generative AI

---

## 🧠 Future Features

- Habit history & streak tracking
- Chat-style conversation interface
- Wearable integration (Apple Health, Fitbit)
- Personalized tips from gut/genetic data

---

## 📄 License

This project is licensed under the MIT License.
