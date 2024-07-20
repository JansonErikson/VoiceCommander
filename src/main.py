import tkinter as tk
from gui import TransparentChatWindow
from stt import VoskSpeechToText
from actions import execute_action
import os
import sys

repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(repo_path, "model", "vosk-model-de-0.21")

def on_speech_result(text):
    chat_app.on_speech_result(text)
    execute_action(text)

if __name__ == "__main__":
    root = tk.Tk()
    stt = VoskSpeechToText(model_path, on_speech_result)
    chat_app = TransparentChatWindow(root, stt)


    def on_close():
        chat_app.stop_speech_recognition()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()