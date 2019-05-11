#!/usr/bin/env python3

import pyaudio
import random
import numpy as np
import matplotlib.pyplot as plt

stream=pyaudio.PyAudio().open(format=pyaudio.paInt8,channels=1,rate=22050,output=True)

def sin(freq,duracion):
	nbuff=int(22050/freq)
	res8=2**8/3
	ntimes=int((duracion*22050)/int(22050/freq/2))
	seno=[int(np.sin(x*np.pi/nbuff)*res8) for x in range(0,nbuff)]
	return seno*ntimes


freq=200
duracion=2
seno=sin(freq,duracion)
#plt.plot(seno)
#plt.show()

bin_seno=''.join(chr(x) for x in seno) #this transforms out into a binary string
stream.write(bin_seno) #which we can then write to the stream in one go.
stream.close()
pyaudio.PyAudio().terminate()
