import tkinter as tk
from TransparentChatWindow import TransparentChatWindow
from VoskSpeechToText import VoskSpeechToText

def execute_command(command):
    # Führe die entsprechende Aktion basierend auf dem erkannten Befehl aus
    if command in actions:
        actions[command]()

if __name__ == "__main__":
    model_path = "path/to/vosk/model"  # Pfad zum Vosk-Modell

    root = tk.Tk()
    chat_app = TransparentChatWindow(root)

    stt = VoskSpeechToText(model_path)
    stt.start_listening()

    def on_close():
        stt.stop_listening()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()