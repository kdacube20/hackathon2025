from transformers import pipeline

# Pipeline de transcripción con Whisper
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribir(audio_path: str):
    result = pipe(audio_path)
    return result['text']

if __name__ == "__main__":
    texto = transcribir("ejemplo.wav")
    print("Transcripción:", texto)
