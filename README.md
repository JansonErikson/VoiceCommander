# VoiceCommander

VoiceCommander is a voice-controlled desktop assistant that allows users to perform various tasks on their Windows computer using voice commands. It utilizes speech recognition technology to interpret voice input and execute corresponding actions.

## Features

- Voice-activated commands for common Windows operations
- Transparent, always-on-top chat window
- Speech-to-text functionality using the Vosk speech recognition engine
- Customizable set of voice commands
- Visual feedback for recognized commands
- Command list display for easy reference

## Key Functions

1. **Desktop Management:**
   - Show desktop
   - Open File Explorer
   - Switch between windows and tabs
   - Close windows

2. **Navigation:**
   - Arrow key simulations (up, down, left, right)
   - Tab and Enter key simulations

3. **System Controls:**
   - Take screenshots
   - Open Start menu
   - Zoom in/out
   - Scroll up/down

4. **Web Browser (Google Chrome) Controls:**
   - Launch Chrome
   - Open new tabs
   - Close tabs
   - Navigate between tabs
   - Open downloads
   - Toggle bookmarks bar

## Installation

1. Clone this repository
2. Install the required dependencies:

pip install -r requirements.txt

Or run the `setup.bat` file.

3. Download the Vosk model for German language and place it in the `model` folder.

Link to all Vosk Models:
https://alphacephei.com/vosk/models

## Usage

1. Run the `start.bat` file or execute `main.py` to start the application.
2. The transparent chat window will appear on your screen.
3. Click the "Record" button to start voice recognition.
4. Speak your commands clearly.
5. The recognized command and its execution will be displayed in the chat window.

## Customization

You can add or modify voice commands by editing the `actions.py` file. The `execute_action` function maps voice commands to their corresponding actions.

## Requirements

- Python 3.7+
- PyAutoGUI
- PyAudio
- Vosk
- Jellyfish

## Note

This project is primarily designed for German language input. To use it with other languages, you'll need to replace the Vosk model and adjust the command recognition accordingly.


## License

[MIT License](LICENSE)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/VoiceCommander/issues) if you want to contribute.