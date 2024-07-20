import tkinter as tk
from gui import TransparentChatWindow
from stt import VoskSpeechToText
from actions import execute_action
import os
import sys
import logging

# Path's
repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(repo_path, "model", "vosk-model-de-0.21")
logging_file = os.path.join(repo_path, "logs", "app.log")

# Logging-Configuration
logging.basicConfig(filename=logging_file, level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



def on_speech_result(text):
    try:
        chat_app.on_speech_result(text)
        execute_action(text)
    except Exception as e:
        logger.error(f"Fehler bei der Verarbeitung des Sprachergebnisses: {str(e)}")

def main():
    global chat_app
    try:
        root = tk.Tk()
        stt = VoskSpeechToText(model_path, on_speech_result)
        chat_app = TransparentChatWindow(root, stt)

        def on_close():
            try:
                chat_app.stop_speech_recognition()
                root.destroy()
            except Exception as e:
                logger.error(f"Fehler beim Schließen der Anwendung: {str(e)}")

        root.protocol("WM_DELETE_WINDOW", on_close)
        logger.info("Anwendung gestartet")
        root.mainloop()
    except Exception as e:
        logger.error(f"Schwerwiegender Fehler in der Hauptfunktion: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()