# 🐚 PromptShell

**PromptShell** is an AI-powered terminal interface built with Streamlit and LangChain, using Google Gemini (via `langchain-google-genai`). It converts natural language into shell commands, executes them, and remembers session history for contextual awareness — just like a smart terminal.

---

## 📦 Features

- 💬 Converts natural language to shell commands using Gemini.
- 🖥️ Executes the command and displays the output.
- 🧠 Remembers command history to improve future suggestions.
- ⚙️ Automatically adapts to your OS (Linux, macOS, Windows).
- 🔒 No local installation of Gemini required — uses Google Generative AI API.

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/promptshell.git
cd promptshell

pip install -r requirements.txt


3. Get Google Gemini API Key
Go to Google AI Studio and:

Create a new API key.

Enable the Generative Language API for your project.

Copy the key.

You can set your API key in code or store it securely with environment variables.


google_api_key = "YOUR_API_KEY"

# To Run the app
streamlit run promptshell.py
