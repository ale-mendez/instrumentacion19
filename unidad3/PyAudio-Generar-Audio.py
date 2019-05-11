#!/usr/bin/env python3

import pyaudio
import random
import numpy as np

stream=pyaudio.PyAudio().open(format=pyaudio.paInt8,channels=1,rate=22050,output=True)

class piano:
	def __init__(self, duracion):
		self.duracion = duracion

	def nota(self, freq):
		n = [0 for x in range(0,int(22050/freq/2))]
		p = [255 for x in range(0,int(22050/freq/2))]
		out = (n+p)*int((self.duracion*22050)/int(22050/freq/2))

		return out

	def silencio(self):
		n = [0 for x in range(0,int(22050))]
		out = (n+n)*int((self.duracion*22050)/int(22050))
		return out

DURACION = 1 #seconds, aproximate.
Cancion = piano(DURACION)

C2 = Cancion.nota(130.813)
D2 = Cancion.nota(146.832)
E2 = Cancion.nota(164.814)
F2 = Cancion.nota(174.614)
G2 = Cancion.nota(195.998)
A2 = Cancion.nota(220)
B2 = Cancion.nota(246.942)
C3 = Cancion.nota(261.626)
D3 = Cancion.nota(293.665)
E3 = Cancion.nota(329.628)
F3 = Cancion.nota(349.228)
G3 = Cancion.nota(391.995)
A3 = Cancion.nota(440)
B3 = Cancion.nota(493.883)

silencio = Cancion.silencio()

out=(A3)


#for val in out:
#        stream.write(chr(val))

# instead of looping, it's probably better to calculate all the data and pass
# it in one go

bin_out=''.join(chr(x) for x in out) #this transforms out into a binary string
stream.write(bin_out) #which we can then write to the stream in one go.

stream.close()
pyaudio.PyAudio().terminate()
