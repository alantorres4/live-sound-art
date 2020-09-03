import numpy as np
import pyaudio

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording devize (Hz)

p = pyaudio.PyAudio() # initialize the p object
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK) # uses default input device

# create a numpy array holding a single read of audio data:
for i in range(10): # do it a few times just to see
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    print(data)

# close the stream 
stream.stop_stream()
stream.close()
p.terminate