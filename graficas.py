# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import math

from metodos import eq_diferenciales
from metodos import transformada_fourier

from numpy import fft

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

	#se obtienen un muestreo de valores por periodo (muestreo + 1)
	muestreo = 3
	paso = int(math.ceil(pasos_periodo) / float(muestreo))
	muestra = []
	for i, (_, x, _) in enumerate(sol_numerica):
		if i % paso == 0:
			muestra.append(x)

	fourier_promediado = [0] * (muestreo + 1)
	# se obtiene la Transformada de Fourier Discreta para cada periodo
	for i in range(fourier_periodos):
		# se determina el inicio y fin de cada periodo
		inicio_periodo = i * muestreo
		final_periodo = inicio_periodo + muestreo + 1
		print 'Periodo: ', muestra[inicio_periodo:final_periodo]
		fourier = transformada_fourier.tfd(muestra[inicio_periodo:final_periodo])
		#se acumulan los coeficientes promediados obtenidos por cada periodo
		for k, c in enumerate(fourier):
			fourier_promediado[k] += c / float(fourier_periodos)
		
	# se obtiene la potencia calculando el módulo de cada coeficiente complejo
	espectro_potencia = []
	for c in fourier_promediado:
		p = (c * c.conjugate()).real
		espectro_potencia.append(p)

	n = range(len(espectro_potencia))
	plt.subplot(212)
	plt.plot(n, espectro_potencia, 'b^')
	plt.vlines(n, [0], espectro_potencia, 'b')
	plt.title('Espectro de potencia')
	plt.xlabel('Frecuencias constitutivas [n]')
	plt.xticks(n)
	plt.ylabel('Potencia [J/s]')

	plt.tight_layout()

	if fichero is not None:
		plt.savefig(fichero)

	plt.show()
