# -*- coding: utf8 -*- 

from metodos import eq_diferenciales
import math
import matplotlib.pyplot as plt

def f(x, y, t):
	return y

def g(x, y, t):
	return -x

h = 0.05
periodo = 2.0 * math.pi 
n = int(1 * periodo / h)
sol_numerica = eq_diferenciales.runge_kutta_sistema(h, n, f, g, 1.0, 0.0, 0.0)

tiempo = []
numerica = []
analitica = []
for t, x, _ in sol_numerica:
	tiempo.append(t)
	numerica.append(x)

plt.plot(tiempo, numerica, label='Solución numérica')

plt.show()