import eq_diferenciales

def f(x, y, t):
	return x * y + t

def g(x, y, t):
	return t * y + x

print 'Metodo Runge-Kutta Sistema de Ecuaciones'
eq_diferenciales.runge_kutta_sistema(0.1, 5, f, g, 1.0, -1.0, 0.0, verbose=True)