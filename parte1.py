import numpy as np 
import matplotlib.pyplot as plt 
import math
n = 100
x = 1.705
delta = np.logspace(-1, -15, n , dtype="float32" )

m_simple = np.arange(0, n, dtype="float32")
m_h4 = np.arange(0, n , dtype="float32")
k = 0
while k < len(delta):
    dt = delta[k]
    m_simple[k]= (np.cos(x)-np.cos(x+dt))/dt
    m_h4[k] = (np.cos(x + 2* dt)-8*np.cos(x + dt)+8*np.cos(x - dt)\
    -np.cos(x -2* dt))/(12 * dt)
    k = k+1

