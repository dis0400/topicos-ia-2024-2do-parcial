import sys
import os
import gradio as gr
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_assistant.agent import TravelAgent

agent = TravelAgent().get_agent()


def agent_response(message, history):
    return agent.chat(message).response


if __name__ == "__main__":
    demo = gr.ChatInterface(agent_response, type="messages")
    demo.launch()
