# IRIS - Voice-Activated Virtual Assistant 🎙️

IRIS is a lightweight, local Python-based voice assistant inspired by JARVIS. It listens for a specific wake word, handles speech-to-text processing using Google's Speech Recognition API, and performs desktop automation like opening major websites or reading out top news headlines.

---

## ✨ Features
- **Wake Word Detection:** Listens continuously until it hears "Iris".
- **Dynamic TTS:** Uses `pyttsx3` for offline Text-to-Speech synthesis.
- **Web Automation:** Opens popular platforms (Google, YouTube, Instagram, X, LinkedIn, Facebook) via voice commands.
- **Live News Feed:** Fetches real-time global headlines using the NewsAPI framework.

---

## 📦 Prerequisites & Installation

Before running the project, you need to install Python (3.8+ recommended) and the necessary dependencies.

### 1. Install System Audio Dependencies
If you encounter errors installing `pyaudio`, you may need to install the audio development libraries for your OS first:
- **macOS:** `brew install portaudio`
- **Linux (Ubuntu/Debian):** `sudo apt-get install python3-pyaudio portaudio19-dev`

### 2. Clone the Repository
```bash
git clone [https://github.com/your-username/IRIS-voice-assistant.git](https://github.com/your-username/IRIS-voice-assistant.git)
cd IRIS-voice-assistant
