#!/usr/bin/env python3

import visa
import matplotlib.pyplot as plt

import numpy as np

rm = visa.ResourceManager()
instruments=rm.list_resources()
 
id_oscilo=instruments[0]
print('id_oscilo=',id_oscilo)

osci=rm.open_resource(id_oscilo)

xze, xin, yze, ymu, yoff = osci.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;', separator=';')

osci.write('DAT:ENC RPB')
osci.write('DAT:WID 1')

data = osci.query_binary_values('CURV?', datatype='B', container=np.array)

tiempo = xze + np.arange(len(data)) * xin

plt.plot(tiempo, data);
plt.xlabel('Tiempo [s]');
plt.ylabel('Voltaje [V]');
