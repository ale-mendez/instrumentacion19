#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.,100,500)

def Gauss(x, Sigma, A, X0):
    y = A*np.exp(-((x-X0)/(2*Sigma))**2)
    return y

plt.plot(x,Gauss(x,0.1,1,10))
plt.plot(x,Gauss(x,1,1,20))
plt.plot(x,Gauss(x,10,1,70))
plt.show()
