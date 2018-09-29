import numpy as np 
import matplotlib.pyplot as plt 
import math

tolerancia=1e-9
def func_planck(x):
    return ((np.tan(x)**3)*(1+np.tan(x)**2))/(np.exp(np.tan(x))-1)
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

I_planck=0
n=5
while np.fabs(simpson_metod(0,np.pi/2,n)-(np.pi**4/15)) > tolerancia:
    I_planck=simpson_metod(0,np.pi/2,n)
    n+=10
#parte 3
data1=np.loadtxt("firas_monopole_spec_v1.txt")
#se crean matrices con los datos del archivo
frecuencia=[]
espectro=[]
incertidumbre=[]
l=0
while l < len(data1):
    # Se transforman las frecuencias a Hertz
    frecuencia.append(data1[l][0]*300)
    espectro.append(data1[l][1])
    incertidumbre.append(data1[l][3])
    l += 1

def trapecio(x1,x2,y1,y2):
    return (x2-x1)*(y1+y2)/2

I_trapecio=0
k=0
while k < len(frecuencia)-1:
    a=frecuencia[k]
    b=frecuencia[k+1]
    ay=espectro[k]
    by=espectro[k+1]
    I_trapecio+=trapecio(a,b,ay,by)
    k += 1

c= 3e8
h= 6.626e-34
kb=1.38e-23
Tk=(((c**2)*(h**3)*I_trapecio)/(2*(kb**4)*I_planck))**(1/4)
def B_v(t, frec):
    return((2*h*frec**3)/c**2)/(np.exp((h*frec)/kb*t)-1)
B_275=[]
B_exp=[]
k=0
while k < len(frecuencia) :
    B_275.append(B_v(2725,frecuencia[k]))
    B_exp.append(B_v(Tk,frecuencia[k]))
    k += 1
fig, ax =plt.subplots()
ax.errorbar(frecuencia, espectro, yerr=incertidumbre, label="FIRAS")
plt.xlabel("Hz")
plt.ylabel("$\\frac{KJy}{sr}$")
plt.title("Gráfico espectro medido por el FIRAS[$\\frac{KJy}{sr}$] v/s frecuencia[Hz]")
plt.plot(frecuencia, B_275, label="2725 K")
plt.plot(frecuencia, B_exp, label="Tk")
plt.legend()
plt.show()
