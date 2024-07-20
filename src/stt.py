import pyaudio
import json
from vosk import Model, KaldiRecognizer
import threading
import queue
from actions import execute_action, actions

class VoskSpeechToText:
    def __init__(self, model_path, sample_rate=16000):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)
        self.sample_rate = sample_rate
        self.chunk_size = 1024
        self.audio = pyaudio.PyAudio()
        self.running = False
        self.audio_queue = queue.Queue()

    def start_listening(self):
        self.running = True
        self.listening_thread = threading.Thread(target=self._listen)
        self.processing_thread = threading.Thread(target=self._process_audio)
        self.listening_thread.start()
        self.processing_thread.start()

    def stop_listening(self):
        self.running = False
        self.listening_thread.join()
        self.processing_thread.join()

    def _listen(self):
        stream = self.audio.open(format=pyaudio.paInt16,
                                 channels=1,
                                 rate=self.sample_rate,
                                 input=True,
                                 frames_per_buffer=self.chunk_size)

        while self.running:
            data = stream.read(self.chunk_size)
            self.audio_queue.put(data)

        stream.stop_stream()
        stream.close()

    def _process_audio(self):
        while self.running:
            data = self.audio_queue.get()
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                if 'text' in result:
                    self._check_keywords(result['text'])

    def _check_keywords(self, text):
        words = text.lower().split()
        for word in words:
            if word in actions:
                execute_action(word)
                break  # Führe nur die Aktion für das erste erkannte Keyword aus

    def __del__(self):
        self.audio.terminate()

# Beispielverwendung
if __name__ == "__main__":
    model_path = "path/to/vosk/model"  # Pfad zum Vosk-Modell
    
    stt = VoskSpeechToText(model_path)
    stt.start_listening()

    # Simuliere eine laufende Anwendung
    import time
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Beende Programm...")
        stt.stop_listening()