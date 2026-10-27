import sounddevice as sd

def record_audio():

    # Microphone recording settings
    sample_rate = 16000
    duration = 5
    channels = 1

    # Record audio
    

    recording = sd.rec(
        frames=sample_rate * duration,
        samplerate=sample_rate,
        channels=channels
    )

    # Wait until recording finishes
    sd.wait()


    return recording