# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 30

def record():
    # Start recorder with the given values
    # of duration and sample frequency
    print("Recording")
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    # write("/Users/akshara/Desktop/hoop/vprof/gender-recognition-by-voice/Data/recording0.wav", freq, recording)

    return{
    wv.write("/Users/hlabs/Desktop/hoop/voicebot/gendervoice/recording1.wav", recording, freq, sampwidth=2)
    }

record()