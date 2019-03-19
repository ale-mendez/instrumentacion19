#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.,2.0*np.pi,500)

def fsin(x,omega):
    y = np.sin(x*omega)
    return y

# y = fsin(x,1.0)

plt.plot(x,fsin(x,1.0))
plt.plot(x,fsin(x,2.0))
plt.plot(x,fsin(x,3.0))
plt.show()
