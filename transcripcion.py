from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribir(audio_path: str):
    result = pipe(audio_path)
    return result['text']
