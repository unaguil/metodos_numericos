# -*- coding: utf8 -*- 

from metodos import eq_diferenciales
from metodos import transformada_fourier
import math
import graficas

def f(x, y, t):
	return y

def g(x, y, t):
	return math.cos(t) - x

h = 0.01
num_periodos = 5
graficas.mostrar_graficas(h, num_periodos, f, g, 1.0, 0.0, 0.0, 'oscilador lineal forzado no amortiguado')