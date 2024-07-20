import pyaudio
import json
from vosk import Model, KaldiRecognizer
import threading
import queue
import jellyfish

class VoskSpeechToText:
    def __init__(self, model_path, callback, sample_rate=16000):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)
        self.sample_rate = sample_rate
        self.chunk_size = 1024
        self.audio = pyaudio.PyAudio()
        self.running = False
        self.audio_queue = queue.Queue()
        self.callback = callback
        self.available_commands = [
            "desktop", "explorer", "switchen", "tab wechseln", "übersicht",
            "fenster schließen", "screenshot", "pfeil hoch", "pfeil runter",
            "pfeil links", "pfeil rechts", "weiter", "enter", "windows",
            "plus", "minus", "auf", "ab", "chrome", "neuer tab",
            "tab schließen", "nächster tab", "tab zurück", "downloads öffnen",
            "lesezeichen"
        ]

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
        if len(text.strip()) > 3:  # Ignoriere sehr kurze Erkennungen
            best_match = self.find_best_match(text, self.available_commands)
            if best_match:
                self.callback(best_match)
            else:
                self.callback(text)

    @staticmethod
    def find_best_match(input_text, commands, threshold=0.7):
        best_match = None
        best_score = 0

        for command in commands:
            score = jellyfish.jaro_winkler_similarity(input_text.lower(), command.lower())
            if score > best_score and score >= threshold:
                best_score = score
                best_match = command

        return best_match

    def __del__(self):
        if hasattr(self, 'audio'):
            self.audio.terminate()