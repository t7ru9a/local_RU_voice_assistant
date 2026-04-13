import pyaudio
import numpy as np
import keyboard
import config

def record_audio_stream():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=config.CHANNELS, 
                    rate=config.RATE, input=True, frames_per_buffer=config.CHUNK)
    
    frames = []
    print("\n[ЗАПИСЬ...] Говорите...")

    while keyboard.is_pressed(config.HOTKEY):
        data = stream.read(config.CHUNK)
        frames.append(data)

    print("[ОБРАБОТКА...]")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Конвертация в float32 для Whisper
    audio_data = b''.join(frames)
    return np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0