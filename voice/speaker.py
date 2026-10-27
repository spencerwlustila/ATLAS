import subprocess

def speak(text):

    speech_rate = "180"
    subprocess.run(["say", "-v", "Daniel", "-r", speech_rate, text])











if __name__ == "__main__":
    speak("Hello. All systems operational.")