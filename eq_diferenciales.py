
def runge_kutta(h, n, f, x_0, y_0, verbose=False):
	x = x_0
	y = y_0

	for i in range(n + 1):
		k1 = h * f(x, y)
		k2 = h * f(x + h / 2, y + k1 / 2)
		k3 = h * f(x + h / 2, y + k2 / 2)
		k4 = h * f(x + h, y + k3)

		if verbose: print "%.1f \t %.5f \t %.4f \t %.4f \t %.4f \t %.4f" % (x, y, k1, k2, k3, k4)

		y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
		x += h

	return x, y


def calcular_estimaciones(h, f, x, y, t, verbose=False):
	k1 = h * f(x, y, t)
	k2 = h * f(x + h / 2, y + k1 / 2, t)
	k3 = h * f(x + h / 2, y + k2 / 2, t)
	k4 = h * f(x + h, y + k3, t)

	if verbose: print "%.5f \t %.5f \t %.5f \t %.5f \t %.5f \t %.5f \t %.5f" % (t, x, y, k1, k2, k3, k4)

	return k1, k2, k3, k4

def runge_kutta_sistema(h, n, f, g, x_0, y_0, t_0, verbose=False):
	t = t_0
	x = x_0
	y = y_0

	for i in range(n + 1):
		kx1, kx2, kx3, kx4 = calcular_estimaciones(h, f, x, y, t, verbose)
		ky1, ky2, ky3, ky4 = calcular_estimaciones(h, g, x, y, t, verbose)

		x = x + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
		y = y + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6

		t += h

	return t, x, y