import sounddevice as sd

def record_audio():

    # Microphone recording settings
    sample_rate = 16000
    duration = 5
    channels = 1

    # Record audio
    print("ATLAS: Recording...")

    recording = sd.rec(
        frames=sample_rate * duration,
        samplerate=sample_rate,
        channels=channels
    )

    # Wait until recording finishes
    sd.wait()

    # Confirm recording
    print("ATLAS: Recording complete!")
    print(recording.shape)

    return recording