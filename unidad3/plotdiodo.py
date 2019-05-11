#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
diodopositivo = pd.read_csv("diodo-positivo.txt")
compu = pd.read_csv("diodo-positivo-PC.txt")
fig=plt.figure(figsize = (15, 10))
plt.plot(np.exp(compu))
#plt.savefig('compu.eps', format='eps', bbox_inches='tight')
plt.show()
