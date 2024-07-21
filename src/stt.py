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
            "kommandos",
            "desktop", "explorer", "switchen", "tab wechseln", "übersicht",
            "fenster schließen", "screenshot", "nord", "süd",
            "west", "ost", "weiter", "bestätigen", "windows",
            "plus", "minus", "runter", "hoch", "internet", "neuer tab",
            "tab schließen", "nächster tab", "tab zurück", "downloads öffnen",
            "lesezeichen"
        ]
        self.banned_keywords = [
            "der", "die", "das", "ein", "eine", "einen", "und", "oder", "aber", "wenn", "dann",
            "für", "mit", "von", "zu", "in", "an", "auf", "über", "unter", "vor",
            "nach", "bei", "um", "durch", "aus", "zum", "zur", "am", "im", "Ayten", "Duyal", "danke" 
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
        words = text.lower().split()
        filtered_words = [word for word in words if word not in self.banned_keywords]
        
        if len(filtered_words) > 0:
            if len(filtered_words) >= 2:
                # Prüfe auf Teilübereinstimmungen mit Befehlen
                for i in range(len(filtered_words)):
                    for j in range(i+1, len(filtered_words)+1):
                        phrase = " ".join(filtered_words[i:j])
                        best_match = self.find_best_match(phrase, self.available_commands)
                        if best_match:
                            self.callback(best_match)
                            return

            # Wenn kein Befehl gefunden wurde, prüfe das gesamte gefilterte Text
            best_match = self.find_best_match(" ".join(filtered_words), self.available_commands)
            if best_match:
                self.callback(best_match)
            else:
                self.callback(" ".join(filtered_words))

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