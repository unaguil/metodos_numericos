
def runge_kutta(h, n, f, x_0, y_0):
	x = x_0
	y = y_0
	for i in range(n + 1):
		k1 = h * f(x, y)
		k2 = h * f(x + h / 2, y + k1 / 2)
		k3 = h * f(x + h / 2, y + k2 / 2)
		k4 = h * f(x + h, y + k3)
		new_y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

		print "%.1f \t %.5f \t %.4f \t %.4f \t %.4f \t %.4f" % (x, y, k1, k2, k3, k4)
		x += h
		y = new_y

def df_dx(x, y):
	return -2 * x -y

print 'Metodo Runge-Kutta'
runge_kutta(0.1, 5, df_dx, 0.0, -1.0)