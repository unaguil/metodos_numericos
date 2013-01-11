# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import math

from metodos import eq_diferenciales
from metodos import transformada_fourier

def mostrar_graficas(h, num_periodos, f, g, x_0, y_0, t_0, titulo):
	periodo = 2.0 * math.pi 
	n = int(num_periodos * periodo / h)
	sol_numerica = eq_diferenciales.runge_kutta_sistema(h, n, f, g, x_0, y_0, t_0)

	tiempo = []
	numerica = []
	analitica = []
	for t, x, _ in sol_numerica:
		tiempo.append(t)
		numerica.append(x)

	plt.plot(tiempo, numerica, label='Solución numérica')
	plt.title('Movimiento del %s' % titulo)
	plt.xlabel('t [rad]')
	plt.ylabel('x')
	plt.show()

	plt.clf()

	x = [x for _, x, y in sol_numerica]
	trans_fourier = transformada_fourier.tfd(x)

	espectro_potencia = []
	for c in trans_fourier:
		p = (c * c.conjugate()).real
		espectro_potencia.append(p)

	n = range(len(espectro_potencia))
	plt.plot(n, espectro_potencia)
	plt.title('Espectro de potencia del %s' % titulo)
	plt.xlabel('Componentes')
	plt.ylabel('Potencia')
	plt.show()