import os
import shutil
import time

AUDIO_DIR = "static"
os.makedirs(AUDIO_DIR, exist_ok=True)

def save_audio_file(file):
    filename = f"audio_{int(time.time())}.wav"
    file_path = os.path.join(AUDIO_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return filename

def get_audio_url(filename):
    return f"/static/{filename}"
