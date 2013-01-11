# -*- coding: utf8 -*- 

import matplotlib.pyplot as plt
from numpy import arange, pi, sin
import csv
import test_runge_kutta_sistema

test_runge_kutta_sistema.lanzar_metodo()

csvreader = csv.reader(open('test.dat'), delimiter='\t')
tiempo = []
numerica = []
analitica = []
error = []
for line in csvreader:
	tiempo.append(line[0])
	numerica.append(line[1])
	analitica.append(line[2])
	error.append(line[3])

plt.plot(tiempo, numerica, label='Solución numérica')
plt.plot(tiempo, analitica, label='Solución analítica')

plt.show()
