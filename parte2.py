import numpy as np 
import matplotlib.pyplot as plt 
import math
data = np.loadtxt("firas_monopole_spec_v1.txt")
#se crean matrices con los datos del archivo
frecuencia=[]
espectro=[]
incertidumbre=[]
k=0
while k < len(data):
    # Se transforman las frecuencias a Hertz
    frecuencia.append(data[k][0]*100*3e8)
    espectro.append(data[k][1])
    incertidumbre.append(data[k][3])
    k += 1
#se plotea con los errores(incertidumbre) ponderados a 400
#fltan titles#############
fig, ax =plt.subplots()
ax.errorbar(frecuencia, espectro, yerr=incertidumbre)
plt.xlabel("Hz")
plt.ylabel("Espectro[$\\frac{KJy}{sr}$]")
#plt.show()

"""
2.
"""
tolerancia=1e-60
def func_planck(x):
    return ((np.tan(x)**3)*(1+np.tan(x)**2))/(np.e**(np.tan(x))-1)
def simpson_metod(x1,x2,n,func):
    paso=(x2-x1)/(2*n)
    sum_par=0
    sum_impar=0
    i = 1
    while i < 2*n:

        if i%2 == 0:
            sum_par += func(x1+i*paso)
        else:
            sum_impar += func(x1+i*paso)
        i += 1
    return (paso/3)*(func(x1+(paso/2))+2*sum_impar+4*sum_par+func(x2-(paso/2)))