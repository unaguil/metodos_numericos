import eq_diferenciales
import math

def f(x, y, t):
	return y

def g(x, y, t):
	return -x

def lanzar_metodo():
	h = 0.01
	periodo = 2.0 * math.pi 
	n = int(1 * periodo / h)
	sol_numerica = eq_diferenciales.runge_kutta_sistema(h, n, f, g, 1.0, 0.0, 0.0)

	sol_analitica = []
	for t, _, _ in sol_numerica:
		sol_analitica.append(math.cos(t))

	file = open('test.dat', 'w')
	for i, ((t, x_n, _), x_a) in enumerate(zip(sol_numerica, sol_analitica)):
		file.write('%.2f,%.6f,%.6f,%.6f\n' % (t, x_n, x_a, x_n - x_a))
	file.close()

lanzar_metodo()
