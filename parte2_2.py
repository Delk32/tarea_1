import numpy as np 
import matplotlib.pyplot as plt 
import math

tolerancia=1e-60
def func_planck(x):
    return ((np.tan(x)**3)*(1+np.tan(x)**2))/(np.e**(np.tan(x))-1)
def simpson_metod(x1,x2,n):
    paso=(x2-x1)/(2*n)
    sum_par=0
    sum_impar=0
    i = 1
    while i < 2*n:

        if i%2 == 0:
            sum_par += func_planck(x1+i*paso)
        else:
            sum_impar += func_planck(x1+i*paso)
        i += 1
    return (paso/3)*(func_planck(x1+(paso/2))+2*sum_impar+4*sum_par+func_planck(x2-(paso/2)))

I=0
n=5
while np.fabs(simpson_metod(0,np.pi/2,n)-(np.pi**4/15)) > tolerancia:
    I=simpson_metod(0,np.pi/2,n)
    n+=10