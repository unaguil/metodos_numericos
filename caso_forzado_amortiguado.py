# -*- coding: utf8 -*- 

from metodos import eq_diferenciales
from metodos import transformada_fourier
import math
import graficas

#definición de las funciones del sistema de ecuaciones diferenciales
def f(x, y, t):
	return y

def g(x, y, t):
	return math.cos(t) - x - 0.52 * y

h = 0.01 # configuración del paso de integración
num_periodos = 5 #periodos de la señal visualizados
x_0 = 0.0 # condición inicial x(t_0) = 0
y_0 = 0.0 # condición inicial dx/dt(t_0) = 0
t_0 = 0.0 # condición inicial t_0 = 0

#cálculo y representación gráfica de la señal y la espectro de potencias
graficas.mostrar_graficas(h, num_periodos, f, g, x_0, y_0, t_0, 'oscilador lineal forzado y amortiguado', 'memoria/caso_forzado_amortiguado.pdf')
