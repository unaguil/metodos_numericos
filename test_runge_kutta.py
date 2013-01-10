import eq_diferenciales

def dy_dx(x, y):
	return -2 * x -y

print 'Metodo Runge-Kutta'
eq_diferenciales.runge_kutta(0.1, 5, dy_dx, 0.0, -1.0, verbose=True)