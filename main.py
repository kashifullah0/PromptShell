import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import subprocess

GEMINI_API_KEY = "AIzaSyBkA9oQFyqX-BEgq1skdzxghxd0_G0494E"

class SmartTerminal:
    def __init__(self):
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=GEMINI_API_KEY)
        self.data = llm.invoke("Are You Working")
    
    def __repr__(self):
        return f"{self.data.content}"



app = SmartTerminal()

print(app)