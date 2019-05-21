#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
diodopositivo = pd.read_csv("DatosDiodo-IvsV.txt",delimiter="\s+",header=None)
fig=plt.figure(figsize = (6, 6))
plt.xlabel('Voltaje (V)',size=14)
plt.ylabel('Corriente (mA)',size=14)
plt.plot(diodopositivo[0],diodopositivo[1]*1E3,'ro',markerfacecolor='none',markersize=4)
plt.savefig('diodo.eps', format='eps', bbox_inches='tight')
#plt.show()
