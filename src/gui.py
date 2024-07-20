import tkinter as tk
from tkinter import scrolledtext, Toplevel
from stt import VoskSpeechToText

class TransparentChatWindow:
    def __init__(self, master, speech_recognition):
        self.master = master
        master.title("VoiceCommander")
        master.attributes('-alpha', 0.7)
        master.attributes('-topmost', True)

        
        # Window size and position
        window_width = 400
        window_height = 100
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = 0  # Top center
        master.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Set background color to black
        master.configure(bg='black')
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(master, state='disabled', bg='black', fg='light blue', height=2)
        self.chat_display.pack(expand=True, fill='both', padx=5, pady=2)
        
        # Input field
        self.msg_entry = tk.Entry(master, bg='black', fg='light blue', insertbackground='light blue')
        self.msg_entry.pack(fill='x', padx=5, pady=1)
        self.msg_entry.bind('<Return>', self.send_message)
        
        # Button frame
        button_frame = tk.Frame(master, bg='black')
        button_frame.pack(fill='x', padx=5, pady=1)
        
        # Send button
        self.send_button = tk.Button(button_frame, text="Send", command=self.send_message, bg='black', fg='light blue')
        self.send_button.pack(side='left', padx=5)
        
        # Record button
        self.record_button = tk.Button(button_frame, text="Record", command=self.toggle_speech_recognition, bg='black', fg='light blue')
        self.record_button.pack(side='left', padx=5)

        # Commands button
        self.commands_button = tk.Button(button_frame, text="Commands", command=self.toggle_commands, bg='black', fg='light blue')
        self.commands_button.pack(side='left', padx=5)

        # Commands window
        self.commands_window = None

        # Speech recognition
        self.speech_recognition = speech_recognition
        self.is_listening = False

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.chat_display.config(state='disabled')
            
            # Scroll only the last line into view
            self.chat_display.yview_moveto(0.99)
            
            self.msg_entry.delete(0, tk.END)

    def toggle_speech_recognition(self):
        if self.is_listening:
            self.stop_speech_recognition()
        else:
            self.start_speech_recognition()

    def start_speech_recognition(self):
        self.speech_recognition.start_listening()
        self.is_listening = True
        self.record_button.config(text="Stop Recording", bg='red')

    def stop_speech_recognition(self):
        self.speech_recognition.stop_listening()
        self.is_listening = False
        self.record_button.config(text="Record", bg='black')

    def on_speech_result(self, text):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"Recognized: {text}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview_moveto(0.99)

    def toggle_commands(self, event=None):
        if self.commands_window is None or not self.commands_window.winfo_exists():
            self.show_commands()
        else:
            self.commands_window.destroy()
            self.commands_window = None

    def show_commands(self):
        self.commands_window = Toplevel(self.master)
        self.commands_window.title("Verfügbare Befehle")
        self.commands_window.attributes('-alpha', 0.7)
        self.commands_window.attributes('-topmost', True)
        
        # Position the window on the right side of the screen
        window_width = 320
        window_height = self.master.winfo_screenheight()
        screen_width = self.master.winfo_screenwidth()
        x = screen_width - window_width
        y = 0
        self.commands_window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        self.commands_window.configure(bg='black')
        
        # List of commands and their descriptions
        commands = [
            ("1. Kommands", "Zeigt die verfügbaren Befehle"),
            ("2. Desktop", "Zeigt den Desktop an"),
            ("3. Explorer", "Öffnet den Datei-Explorer"),
            ("4. Switchen", "Wechselt zum nächsten Fenster"),
            ("5. Tab wechseln", "Wechselt zum nächsten Tab"),
            ("6. Übersicht", "Öffnet die Task-Ansicht"),
            ("7. Fenster Schließen", "Schließt das aktuelle Fenster"),
            ("8. Screenshot", "Erstellt einen Screenshot"),
            ("9. Pfeil Hoch", "Drückt die Pfeiltaste nach oben"),
            ("10. Pfeil Runter", "Drückt die Pfeiltaste nach unten"),
            ("11. Pfeil Links", "Drückt die Pfeiltaste nach links"),
            ("12. Pfeil Rechts", "Drückt die Pfeiltaste nach rechts"),
            ("13. Weiter", "Drückt die Tab-Taste"),
            ("14. Enter", "Drückt die Enter-Taste"),
            ("15. Windows", "Öffnet das Startmenü"),
            ("16. Plus", "Zoomt in"),
            ("17. Minus", "Zoomt aus"),
            ("18. Auf", "Scrollt nach oben"),
            ("19. Ab", "Scrollt nach unten"),
            ("20. Chrome", "Startet Google Chrome"),
            ("21. Neuer Tab", "Öffnet einen neuen Tab in Chrome"),
            ("22. Tab schließen", "Schließt den aktuellen Tab in Chrome"),
            ("23. Nächster Tab", "Wechselt zum nächsten Tab in Chrome"),
            ("24. Tab zurück", "Wechselt zum vorherigen Tab in Chrome"),
            ("25. Downloads öffnen", "Öffnet den Download-Manager in Chrome"),
            ("26. Lesezeichen", "Schaltet die Lesezeichen-Leiste in Chrome um")
        ]
        
        # Create a scrolled text widget to display the commands
        command_display = scrolledtext.ScrolledText(self.commands_window, state='normal', bg='black', fg='light blue')
        command_display.pack(expand=True, fill='both', padx=2, pady=2)
        
        # Insert the commands and descriptions
        for command, description in commands:
            command_display.insert(tk.END, command, 'command')
            command_display.insert(tk.END, f"\n{description}\n")
        
        # Configure tag for green command text
        command_display.tag_configure('command', foreground='green')
        
        command_display.config(state='disabled')
