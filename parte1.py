import numpy as np 
import matplotlib.pyplot as plt 
import math
n = np.float32(100)
delta = np.logspace(0, math.pi, n , dtype="float32" )

def fprimah(x, dt):
    fh = np.float32((np.cos(dt)-np.cos(x-dt))/dt)
    return
    
def fprimah_2(x, dt):
    fh_2 = np.float32((np.cos(x + dt)-8*np.cos(x + dt)+8*np.cos(x - dt)\
    -np.cos(x - dt))/(12 * dt))
    return

