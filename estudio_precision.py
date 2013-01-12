# -*- coding: utf8 -*- 

from metodos import eq_diferenciales
import math

def f(x, y, t):
	return y

def g(x, y, t):
	return 0.516 * math.cos(1.2 * t) - x - 0.52 * y - x * x


num_periodos = 5
x_0 = 0.0
y_0 = 0.0
t_0 = 0.0
periodo = 2.0 * math.pi 

h1 = 0.08
n = int(periodo / h1)
sol_numerica_h1 = eq_diferenciales.runge_kutta_sistema(h1, n, f, g, x_0, y_0, t_0)

h2 = 0.04
n = int(periodo / h2)
sol_numerica_h2 = eq_diferenciales.runge_kutta_sistema(h2, n, f, g, x_0, y_0, t_0)

h3 = 0.02
n = int(periodo / h3)
sol_numerica_h3 = eq_diferenciales.runge_kutta_sistema(h3, n, f, g, x_0, y_0, t_0)

h4 = 0.01
n = int(periodo / h4)
sol_numerica_h4 = eq_diferenciales.runge_kutta_sistema(h4, n, f, g, x_0, y_0, t_0)

h5 = 0.005
n = int(periodo / h5)
sol_numerica_h5 = eq_diferenciales.runge_kutta_sistema(h5, n, f, g, x_0, y_0, t_0)

file = open('precision.txt', 'w')
file.write('\\begin{tabular}{|c|c|c|c|c|c|}\n')
file.write('\hline\n')
file.write('t & $h = 0.08$ & $h = 0.04$ & $h = 0.02$ & $h = 0.01$ & $h = 0.005$ \\\\\n')
file.write('\hline\n')

for k in range(0, 80, 5): 
	print "%.2f \t %.8f \t %.8f \t %.8f \t %.8f \t %.8f" % (sol_numerica_h1[k][0], sol_numerica_h1[k][1],
		sol_numerica_h2[k*2][1], sol_numerica_h3[k*4][1], sol_numerica_h4[k*8][1], sol_numerica_h5[k*16][1])
	file.write("%.2f & %.8f & %.8f & %.8f & %.8f & %.8f \\\\ \n" % (sol_numerica_h1[k][0], sol_numerica_h1[k][1],
		sol_numerica_h2[k*2][1], sol_numerica_h3[k*4][1], sol_numerica_h4[k*8][1], sol_numerica_h5[k*16][1]))

file.write('\hline\n')
file.write('\end{tabular}\n')