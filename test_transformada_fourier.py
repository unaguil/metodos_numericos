# -*- coding: utf8 -*- 

from metodos import transformada_fourier
from metodos import eq_diferenciales
import math
import matplotlib.pyplot as plt

def f(x, y, t):
	return y

def g(x, y, t):
	return -x

h = 0.01
periodo = 2.0 * math.pi 
n = int(1 * periodo / h)
sol_numerica = eq_diferenciales.runge_kutta_sistema(h, n, f, g, 1.0, 0.0, 0.0)

x = [x for _, x, y in sol_numerica]
trans_fourier = transformada_fourier.tfd(x)

espectro_potencia = []
for c in trans_fourier:
	p = (c * c.conjugate()).real
	espectro_potencia.append(p)

n = range(len(espectro_potencia))
plt.plot(n, espectro_potencia)

plt.show()