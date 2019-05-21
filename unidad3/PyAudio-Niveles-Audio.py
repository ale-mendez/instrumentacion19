#!/usr/bin/env python3

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paFloat32
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 5
p = pyaudio.PyAudio()
print('running')

stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,
input=True,frames_per_buffer=FRAMESIZE,input_device_index=4)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = np.fromstring(data, 'Float32')

stream.stop_stream()
stream.close()
p.terminate()
print('done')
plt.plot(np.exp(decoded))
plt.show()
