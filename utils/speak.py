import sys
import io
import wave
import subprocess
from piper import PiperVoice

# Ensure text was passed as an argument
if len(sys.argv) < 2:
    print("Usage: friday-say <text to speak>")
    sys.exit(1)

# Join all arguments so it works both with and without quotes
text = " ".join(sys.argv[1:])

MODEL_PATH = "utils/en_GB-alba-medium.onnx"
voice = PiperVoice.load(MODEL_PATH)

wav_buffer = io.BytesIO()
with wave.open(wav_buffer, "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

subprocess.run(
    ["aplay", "-q", "-"],
    input=wav_buffer.getvalue(),
    check=True
)
