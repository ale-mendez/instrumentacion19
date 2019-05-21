#!/usr/bin/env python3

import pyaudio
import numpy as np
#import matplotlib.pyplot as plt
import sys, os

p=pyaudio.PyAudio()

def step(freq):
   xmax=nbuff
   xfreq=int(xmax/freq/2)
   zero=[0 for x in range(0,xfreq)]
   one=[amp for x in range(0,xfreq)]
   ntimes=int(duration*xfreq*2)
   out=(zero+one)*ntimes
   return np.array(out)

def sine(freq):
   xmax=nbuff
   xfreq=int(nbuff/freq)
   ntimes=int(duration*xfreq)
   x=np.arange(xfreq*ntimes)
   out=amp*np.sin(2*np.pi*x*freq/nbuff)
   return out.astype(np.float32)

# type of wave
#     itype = 0 : square function
#           = 1 : sinusoidal function
itype=1
freq=10000.0        # sine frequency, Hz, may be float
duration=10.0      # in seconds, may be float

amp=2**8/2
volume=1.0        # range [0.0, 1.0] * amp
if itype==0: nbuff=22000       # int8 sampling rate, Hz, must be integer
if itype==1: nbuff=44100       # float32 sampling rate, Hz, must be integer

if itype==0: 
    samples=step(freq)
    ftype=pyaudio.paInt8
if itype==1: 
    samples=sine(freq)
    ftype=pyaudio.paFloat32

stream=p.open(format=ftype,channels=2,rate=nbuff,output=True)
#bin_out=''.join(chr(x) for x in samples)
#stream.write(bin_out)
stream.write(samples)

stream.stop_stream()
stream.close()
p.terminate()

# plot sample
#plt.plot(samples,color='black', linestyle='solid',linewidth=2, markersize=12)
#plt.show()

