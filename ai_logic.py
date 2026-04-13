import subprocess
from faster_whisper import WhisperModel
import lmstudio as lms
import config

class AIAssistant:
    def __init__(self):
        self.whisper = WhisperModel(config.WHISPER_MODEL_SIZE, device=config.WHISPER_DEVICE, compute_type="float16")
        self.llm = lms.llm()
        self.chat = lms.Chat(config.LLM_SYSTEM_PROMPT)

    def transcribe(self, audio_np):
        segments, _ = self.whisper.transcribe(audio_np, language="ru")
        return "".join([segment.text for segment in segments]).strip()

    def get_llm_response(self, text):
        self.chat.add_user_message(text)
        return str(self.llm.respond(self.chat))

    def speak(self, text):
        command = ["piper", "--m", config.ACTIVE_VOICE, "--", text]
        subprocess.run(command)