#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.,2.0*np.pi,500)

def fsin(x,omega):
    y = np.sin(x*omega)
    return y

def Gauss(x, Sigma, A, X0):
    y = A*np.exp(-((x-X0)/(2*Sigma))**2)
    return y

y = fsin(x,1.0)

plt.plot(x,y)
plt.plot(x,fsin(x,2.0))
plt.plot(x,Gauss(x,1,1,3))
plt.show()
