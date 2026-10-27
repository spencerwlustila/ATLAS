from faster_whisper import WhisperModel
from voice.microphone import record_audio

# Load the speech recognition model
model = WhisperModel("base.en")


def transcribe_audio():


    # Record audio from microphone
    audio = record_audio()

    # Convert audio into speech segments
    segments, info = model.transcribe(
        audio.flatten(),
        vad_filter=True
        )

    # Store the complete transcription
    transcription = ""



    # Combine all recognized speech segments
    for w in segments:
        transcription += w.text



    return transcription


#test
if __name__ == "__main__":
    result = transcribe_audio()
    print("ATLAS heard:", result)