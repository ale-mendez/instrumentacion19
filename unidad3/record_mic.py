from ast import literal_eval

import pyaudio
import wave
import sys
import matplotlib.pyplot as plt
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
TARGET_FILE = "filename.wav" # Change as required
DEVICE = 1 # use list_devices() to determine

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE,
                input=True,
                output=False) 
                # output flag: do you want the audio to playback over speaker? Be wary of audio feedback if you set to True.

# read data
#data = stream.readframes(CHUNK)

# process stream
save_data = []
record = True
while record:
    data = stream.read(CHUNK)
    save_data.append(data)
    ### TO DO:
    ### Insert your audio processing logic here
    ###
    record = False # At some point stop your recording!

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()

#print(np.size(save_data),type(save_data))
#sys.exit()

float_str =save_data[0]
print(float_str)
result = float(literal_eval(float_str))
print(result)

sys.exit()
#data2=np.fromstring(save_data,'Float32')

plt.plot(result)
plt.show()



# save to file
wf = wave.open(TARGET_FILE, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(save_data))
wf.close()
