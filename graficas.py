# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import math

from metodos import eq_diferenciales
from metodos import transformada_fourier

from numpy import fft

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
	plt.xlabel('Tiempo [rad]')
	plt.ylabel('x(t)')
	plt.show()

	plt.clf()

	x = [x for _, x, y in sol_numerica]
	trans_fourier = fft.fft(x)

	espectro_potencia = []
	for c in trans_fourier:
		p = (c * c.conjugate()).real
		espectro_potencia.append(p)

	n = range(len(espectro_potencia))
	max = 20
	plt.plot(n[:max], espectro_potencia[:max], 'b,')
	plt.vlines(n[:max], [0], espectro_potencia[:max], 'b')
	plt.title('Espectro de potencia del %s' % titulo)
	plt.xlabel('Frecuencias')
	plt.xticks(n[:max])
	plt.ylabel('Potencia')
	plt.show()
