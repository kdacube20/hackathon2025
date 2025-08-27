from transformers import pipeline

<<<<<<< HEAD
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribir_2(audio_path: str):
    result = pipe(audio_path)
    return result['text']
=======
# Pipeline de transcripción con Whisper
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribir(audio_path: str):
    result = pipe(audio_path)
    return result['text']

if __name__ == "__main__":
    texto = transcribir("ejemplo.wav")
    print("Transcripción:", texto)
>>>>>>> 0ffe94212b50bfa3e299da678eb023f0ef0fd93a
