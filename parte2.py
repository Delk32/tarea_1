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
    paso=(x2-x1)/(n*2)
    
sum_pares=0
sum_impares=0
