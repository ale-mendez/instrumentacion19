#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cuadrada1 = pd.read_csv("slewrate_0.5V_1kHz_cuadrada_cerca.txt",delimiter="\s+",header=None)
cuadrada2 = pd.read_csv("slewrate_1V_1kHz_cuadrada_cerca.txt",delimiter="\s+",header=None)
cuadrada3 = pd.read_csv("slewrate_5V_1kHz_cuadrada_cerca.txt",delimiter="\s+",header=None)

fig = plt.figure(figsize=(12,6))
grid = plt.GridSpec(1, 2, wspace=0.2, hspace=0.1)
ax1 = plt.subplot(grid[0, 0])
#ax1.set_title("(a)")
ax1.plot(cuadrada1[0]*1E6,cuadrada1[3]*0.8772-0.02,'ro',markerfacecolor='none',markersize=4,label='Entrada')
ax1.plot(cuadrada1[0]*1E6,cuadrada1[1]*0.8772-0.01,'bo',markerfacecolor='none',markersize=4,label='Salida')
ax1.set_xlabel('Tiempo ($\mu$s)',size=14)
ax1.set_ylabel('Voltaje (V)',size=14)

plt.legend(loc='upper left')

ax2 = plt.subplot(grid[0, 1])#, sharey=ax1)
#ax2.set_title("(b)")
ax2.plot(cuadrada3[0]*1E6,cuadrada3[3]*0.8945-0.12,'ro',markerfacecolor='none',markersize=4,label='Entrada')
ax2.plot(cuadrada3[0]*1E6,cuadrada3[1]*0.8945-0.06,'bo',markerfacecolor='none',markersize=4,label='Salida')
ax2.set_xlabel('Tiempo ($\mu$s)',size=14)
ax2.set_ylabel('Voltaje (V)',size=14)

plt.legend(loc='upper left')

plt.savefig('slewrate.eps', format='eps', bbox_inches='tight')
