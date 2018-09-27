import numpy as np 
import matplotlib.pyplot as plt 
import math
n = 15
x = 1.812
delta = np.logspace(-1, -15, n , dtype="float32" )

m_simple = np.arange(0, n, dtype="float32")
m_h4 = np.arange(0, n , dtype="float32")
k = 0
while k < len(delta):
    dt = delta[k]
    m_simple[k]= (np.cos(x)-np.cos(x+dt))/dt
    m_h4[k] = (np.cos(x + 2* dt)- 8*np.cos(x + dt)+8*np.cos(x - dt)\
    -np.cos(x - 2* dt))/(12 * dt)
    k = k+1

m_simple -= math.sin(x)
m_h4 -= math.sin(x)
plt.plot(delta, np.fabs(m_simple), label="método O(h)")
plt.plot(delta, np.fabs(m_h4), label="método con O($h^4$)")
plt.axhline(0, color='0.8')
plt.yscale('log')
plt.xscale('log')
plt.ylabel("$\\frac{d(-cos(1.705))}{dx}-sin(1.705)$", fontsize="10")
plt.xlabel("$\\delta$x", fontsize="15")
plt.title("Gráfico comparación valor estimado con nominal v/s $\delta$x en float32")
_ = plt.xticks(delta[::2])
plt.legend()
plt.show()



x = 1.812
delta_64 = np.logspace(-1, -15, n , dtype="float64" )

m_simple_64 = np.arange(0, n, dtype="float64")
m_h4_64 = np.arange(0, n , dtype="float64")
k = 0
while k < len(delta):
    dt = delta[k]
    m_simple_64[k]= (np.cos(x)-np.cos(x+dt))/dt
    m_h4_64[k] = (np.cos(x + 2* dt)- 8*np.cos(x + dt)+8*np.cos(x - dt)\
    -np.cos(x - 2* dt))/(12 * dt)
    k = k+1

m_simple_64 -= math.sin(x)
m_h4_64 -= math.sin(x)
plt.plot(delta_64, np.fabs(m_simple_64), label="método O(h)")
plt.plot(delta_64, np.fabs(m_h4_64), label="método con O($h^4$)")
plt.axhline(0, color='0.8')
plt.yscale('log')
plt.xscale('log')
plt.ylabel("$\\frac{d(-cos(1.705))}{dx}-sin(1.705)$", fontsize="10")
plt.xlabel("$\\delta$x", fontsize="15")
plt.title("Gráfico comparación valor estimado con nominal v/s $\delta$x en float64")
_ = plt.xticks(delta[::2])
plt.legend()
plt.show()