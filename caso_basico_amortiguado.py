# -*- coding: utf8 -*- 

from metodos import eq_diferenciales
from metodos import transformada_fourier
import math
import graficas

def f(x, y, t):
	return y

def g(x, y, t):
	return -0.5 * y - x

h = 0.01
num_periodos = 5
x_0 = 1.0
y_0 = 0.0
t_0 = 0.0
graficas.mostrar_graficas(h, num_periodos, f, g, x_0, y_0, t_0, 'oscilador lineal no forzado pero amortiguado')