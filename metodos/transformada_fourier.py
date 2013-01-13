# -*- coding: utf8 -*-

import cmath
import math

def tfd(x):
	'''
		Implementación de la Transformada de Fourier Discreta.
		En el calculo se utiliza la aritmética de numéros complejos
		proporcionada por Python y la librería cmath que incluye otras
		funciones matemáticas para números complejos.
		Devuelve el espectro de frecuencias en una lista
		x : lista que contiene las muestras de un periodo de la señal
	'''
	N = len(x)
	espectro_freq = []
	for n in range(N):
		c = 0
		for k in range(N):
			c += x[k] * cmath.exp(-2j * cmath.pi * n * k / N)
		espectro_freq.append(c)

	return espectro_freq 

def muestrear(sol_numerica, muestras_periodo, pasos_periodo):
	'''
		LLeva a cabo un muestreo de una señal.
		Devuelve una lista con la muestra resultante.
		sol_numerica: contiene la solución numerica obtenida de la
		aplicación del algoritmo de Runge-Kutta
		muestras_periodo: el número de muestras por periodo a obtener
		pasos_periodo: el número de pasos que contiene cada perido
	'''
	#se obtienen un muestreo de valores por periodo muestras_periodo
	paso = int(math.ceil(pasos_periodo) / float(muestras_periodo - 1))
	muestra = []
	for i, (_, x, _) in enumerate(sol_numerica):
		if i % paso == 0:
			muestra.append(x)

	return muestra

def tfd_promedio(fourier_periodos, muestras_periodo, muestra):
	'''
		Calcula la Transformada de Fourier Discreta promediada
		entre varios periodos de la señal.
		Devuelve una lista con la Transformada de Fourier Discreta
		promediada sobre el número de periodos.
		fourier_periodos: el número de periodos de la señal
		muestras_periodo: el número de muestras en cada periodo
		muestras: lista que contiene la muestra a promediar
	'''
	fourier_promediado = [0] * muestras_periodo
	# se obtiene la Transformada de Fourier Discreta para cada periodo
	for i in range(fourier_periodos):
		# se determina el inicio y fin de cada periodo
		inicio_periodo = i * (muestras_periodo - 1)
		final_periodo = inicio_periodo + muestras_periodo
		#calculo de la transformada de Fourier del periodo actual
		fourier = tfd(muestra[inicio_periodo:final_periodo])
		#se acumulan los coeficientes promediados obtenidos por cada periodo
		for k, c in enumerate(fourier):
			fourier_promediado[k] += c / float(fourier_periodos)

	return fourier_promediado

def espectro_pot(fourier):
	'''
		Calcula el espectro de potencia de una lista que contiene
		la Transformada de Fourier Discreta. Utiliza la arimética de
		números complejos proporcionada por el lenguaje Python.
		Devuelve una lista con el espectro de potencias.
		fourier: lista conteniendo la Transformada de Fourier Discreta.
	'''
	# se obtiene la potencia calculando el módulo de cada coeficiente complejo
	espectro_potencia = []
	for c in fourier:
		p = (c * c.conjugate()).real
		espectro_potencia.append(p)

	return espectro_potencia