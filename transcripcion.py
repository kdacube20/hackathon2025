from transformers import pipeline

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ad6bb954b51e51fe628729c5fa8bad0fc81710cd
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribir_2(audio_path: str):
    result = pipe(audio_path)
    return result['text']
<<<<<<< HEAD
=======
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
>>>>>>> ad6bb954b51e51fe628729c5fa8bad0fc81710cd
