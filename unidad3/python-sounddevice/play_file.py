#!/usr/bin/env python3
"""Load an audio file into memory and play its contents.

NumPy and the soundfile module (http://PySoundFile.rtfd.io/) must be
installed for this to work.

This example program loads the whole file into memory before starting
playback.
To play very long files, you should use play_long_file.py instead.

"""
import sounddevice as sd
import numpy as np

def sin_bis(freq,duration):
    xmax=nbuff
    xfreq=int(nbuff/freq)
    ntimes=int(duration*xfreq)
    x=np.arange(xfreq*ntimes)
    out=amp*np.sin(2*np.pi*x*freq/nbuff)
    return out

nbuff=44100
freq=500
samplerate=1024
duration=100
amp=2**8/3
data=sin_bis(freq,duration)
print(type(data))
sd.play(data,samplerate)

