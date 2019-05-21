#!/usr/bin/env python3

import pyaudio
import random
import numpy as np
import matplotlib.pyplot as plt
import sys, os

stream=pyaudio.PyAudio().open(format=pyaudio.paFloat32,channels=2,rate=22050,output=True)

def sin(freq,duration):
   nbuff=int(22050/freq)
   res8=2**8/3
   ntimes=int((duration*22050)/int(22050/freq/2))
   seno=[np.sin(2*x*np.pi/nbuff) for x in range(0,nbuff)]
   sinarr=np.array(seno)
   return sinarr.astype(np.float32)

def sin_bis(freq):
   xmax=nbuff
   xfreq=int(nbuff/freq)
   ntimes=int(duration*xfreq)
   x=np.arange(xfreq*ntimes)
   print(xfreq*ntimes)
   out=amp*np.sin(2*np.pi*x*freq/nbuff)
   return out.astype(np.float32)

amp=2**8
nbuff=44100 
#freq=200
freq=100.0        # sine frequency, Hz, may be float
duration=10.0       # in seconds, may be float
seno=sin(freq,duration)
print(type(seno),np.size(seno))

seno=sin_bis(freq)
print(type(seno),np.size(seno))
plt.plot(seno,'k-')
plt.show()

sys.exit()

stream.write(seno) #which we can then write to the stream in one go.
stream.close()
pyaudio.PyAudio().terminate()
