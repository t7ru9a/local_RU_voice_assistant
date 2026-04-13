import os
import sys

# Путь к CUDA 12 добавленным через pip
python_root = sys.prefix

CUDA_PATHS = [
    os.path.join(python_root, "Lib", "site-packages", "nvidia", "cublas", "bin"),
    os.path.join(python_root, "Lib", "site-packages", "nvidia", "cudnn", "bin")
]

for path in CUDA_PATHS:
    if os.path.exists(path):
        os.environ["PATH"] += os.pathsep + path

# Настройки аудио
FORMAT_AUDIO = 16  # pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Настройки моделей
WHISPER_MODEL_SIZE = "base"
WHISPER_DEVICE = "cuda"  # или "cpu"

# Базовая директория проекта (путь к папке, где лежит config.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Пути к голосам
VOICES_DIR = os.path.join(BASE_DIR, "resources", "piper-voices")

VOICES = {
    "denis": os.path.join(VOICES_DIR, "ru_RU-denis-medium.onnx"),
    "ruslan": os.path.join(VOICES_DIR, "ru_RU-ruslan-medium.onnx")
}

# Активный голос
ACTIVE_VOICE = VOICES["ruslan"]

# Системный ПРОМПТ
LLM_SYSTEM_PROMPT = "Отвечай кратко. Отвечай просто текстом, без разметки."

# Горячая клавиша
HOTKEY = 'Alt'