import sounddevice as sd
import soundfile as sf

filename = 'PinkPanther60.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing