# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import math

from metodos import eq_diferenciales
from metodos import transformada_fourier

def mostrar_graficas(h, num_periodos, f, g, x_0, y_0, t_0, titulo, fichero=None):
	periodo = 2.0 * math.pi # periodo de la señal periódica
	n = int(num_periodos * periodo / h) # numero de pasos de integración para dibujar num_periodos

	#calculo de la tabla de integracion del sistema 
	sol_numerica = eq_diferenciales.runge_kutta_sistema(h, n, f, g, x_0, y_0, t_0)

	# se obtienen de la tabla de valores los vectores de tiempo, 
	tiempo = []
	numerica = []
	for t, x, _ in sol_numerica:
		tiempo.append(t)
		numerica.append(x)

	# se utiliza matplotlib para generar la gráfica de la señal
	plt.subplot(211)
	plt.plot(tiempo, numerica)
	plt.title('Movimiento del %s' % titulo)
	plt.xlabel('Tiempo [s]')
	plt.ylabel('x(t)')

	# se calcula la señal para 50 periodos
	fourier_periodos = 50
	pasos_periodo = periodo / h
	n = int(fourier_periodos * pasos_periodo) # numero de pasos de integración para muestrear fourier_periodos
	sol_numerica = eq_diferenciales.runge_kutta_sistema(h, n, f, g, x_0, y_0, t_0)

	#se define el número de muestras por periodo
	muestras_periodo = 4
	#se muestrea la señal
	muestra = transformada_fourier.muestrear(sol_numerica, muestras_periodo, pasos_periodo)
	#se obtiene su transformada de Fourier
	fourier = transformada_fourier.tfd_promedio(fourier_periodos, muestras_periodo, muestra)
	# se calcula su espectro de potencia
	espectro_potencia = transformada_fourier.espectro_pot(fourier)

	#generación de la gráfica de espectro de potencias
	n = range(len(espectro_potencia))
	plt.subplot(212)
	plt.plot(n, espectro_potencia, 'r^')
	plt.vlines(n, [0], espectro_potencia, 'r')
	plt.title('Espectro de potencia')
	plt.xlabel('Frecuencias constitutivas [n]')
	plt.xticks(n)
	plt.ylabel('Potencia [J/s]')
	plt.tight_layout()

	#escritura de gráfica en fichero
	if fichero is not None:
		plt.savefig(fichero)

	#visualización de la gráfica
	plt.show()