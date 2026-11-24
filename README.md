# Voice-Assistant

A Python-based AI voice assistant powered by OpenRouter.

## Prerequisites
* **Python 3.8+**
* **Git**
* An **OpenRouter API Key** (Get one at [openrouter.ai](https://openrouter.ai))
* **Audio Dependencies (Linux/macOS):** If your assistant uses microphone input (`PyAudio`) or text-to-speech (`pyttsx3`), make sure system audio packages are installed (see OS instructions below).

---

## Installation & Setup

### 1. Linux (Debian / Ubuntu)
Install system audio dependencies (if using microphone/TTS) and clone the repository:
```bash
sudo apt update
sudo apt install python3-venv python3-dev portaudio19-dev espeak -y

git clone https://github.com/dhritimnn/Voice-Assistant
cd Voice-Assistant
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### 2. Windows (Command Prompt)
```cmd
git clone https://github.com/dhritimnn/Voice-Assistant
cd Voice-Assistant
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

### 3. macOS
```bash
brew install portaudio
git clone https://github.com/dhritimnn/Voice-Assistant
cd Voice-Assistant
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### 4. Android (Termux)
*(Note: Install Termux from F-Droid or GitHub, not the Google Play Store.)*
```bash
pkg update && pkg upgrade -y
pkg install python git build-essential portaudio -y

cd ~
git clone https://github.com
cd Voice-Assistant
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

---

## Configuration (API Key)

Create a `.env` file inside the `utils/` folder and add your OpenRouter API key.

**On Linux / macOS / Termux:**
```bash
touch utils/.env
echo 'KEY="your_openrouter_api_key_here"' > utils/.env
```

**On Windows (Command Prompt):**
```cmd
echo KEY="your_openrouter_api_key_here" > utils\.env
```

---

## Usage

Make sure your virtual environment (`myenv`) is activated, then run:

**Linux / macOS / Termux:**
```bash
python3 Assistant.py
```

**Windows:**
```cmd
python Assistant.py
```

