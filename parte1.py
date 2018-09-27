import numpy as np 
import matplotlib.pyplot as plt 
import math
n = 15
x = 1.705
delta = np.logspace(-1, -20, n , dtype="float32" )

m_simple = np.arange(0, n, dtype="float32")
m_h4 = np.arange(0, n , dtype="float32")
k = 0
while k < len(delta):
    dt = delta[k]
    m_simple[k]= (np.cos(x)-np.cos(x+dt))/dt
    m_h4[k] = (np.cos(x + 2* dt)-8*np.cos(x + dt)+8*np.cos(x - dt)\
    -np.cos(x -2* dt))/(12 * dt)
    k = k+1

m_simple -= math.sin(1.705)
m_h4 -= math.sin(1.705)
plt.plot(delta, np.fabs(m_simple), label="método O(h)")
plt.plot(delta, np.fabs(m_h4), label="método con O($h^4$)")
plt.yscale('log')
plt.xscale('log')
plt.ylabel("$\\frac{d}{dx}[-cos(1.705)]-sin(1.705)$", fontsize="15")
plt.xlabel("$\\delta$x", fontsize="15")
plt.legend()
plt.show()