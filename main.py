import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import subprocess
import platform
import os

GEMINI_API_KEY = "Your Google Gemini APi Key"

class SmartTerminal:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GEMINI_API_KEY
        )
        self.system_os = platform.system()

        if "current_path" not in st.session_state:
            st.session_state.current_path = os.getcwd()

    def generate_command(self, user_input):
        prompt = (
            f"Give me the exact shell command only without any explanation. "
            f"I am using {self.system_os}. Just the command, do not give me quotes or comments. "
            f"The input is: {user_input}"
        ) 
        return self.llm.invoke(prompt).content.strip()

    def run_command(self, command):

        if command.startswith("cd "):
            new_path = command[3:].strip()
            target_path = os.path.abspath(os.path.join(st.session_state.current_path, new_path))
            if os.path.isdir(target_path):
                st.session_state.current_path = target_path
                return f"Changed directory to {st.session_state.current_path}", None
            else:
                return None, f"No such directory: {target_path}"

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                cwd=st.session_state.current_path
            )
            return result.stdout, None
        except subprocess.CalledProcessError as e:
            return None, e.stderr

    def run(self):
        st.title("PromptShell: The Smart AI Terminal")

        user_input = st.text_input("Enter your command description:")

        if user_input:
            command = self.generate_command(user_input)
            st.code(command, language="bash")

            output, error = self.run_command(command)

            if output:
                st.code(output)
            else:
                st.error(f"Error: {error}")


if __name__ == "__main__":
    app = SmartTerminal()
    app.run()