import keyboard
import config
from audio_handler import record_audio_stream
from ai_logic import AIAssistant

def main():
    ai = AIAssistant()
    print(f"Приложение готово. Зажмите '{config.HOTKEY}' для записи голоса.")

    try:
        while True:
            keyboard.wait(config.HOTKEY)
            
            audio_np = record_audio_stream()
            user_text = ai.transcribe(audio_np)
            
            if user_text:
                print(f"Я: {user_text}")
                response = ai.get_llm_response(user_text)
                print(f"LLM: {response}")
                ai.speak(response)
            else:
                print("Голос не распознан.")
    except KeyboardInterrupt:
        print("\nПрограмма остановлена.")

if __name__ == "__main__":
    main()