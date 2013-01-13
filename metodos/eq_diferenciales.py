# -*- coding: utf8 -*- 

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

def runge_kutta_sistema(h, n, f, g, x_0, y_0, t_0, verbose=False):
	t = t_0 # condiciones iniciales del sistema
	x = x_0
	y = y_0

	tabla = [(t, x, y)]

	for i in range(n + 1): #bucle hasta el número de pasos indicado
		k1 = h * f(x, y, t) #cálculo de los coeficientes
		l1 = h * g(x, y, t)

		k2 = h * f(x + k1 / 2, y + l1 / 2, t + h / 2)
		l2 = h * g(x + k1 / 2, y + l1 / 2, t + h / 2)

		k3 = h * f(x + k2 / 2, y + l2 / 2, t + h / 2)
		l3 = h * g(x + k2 / 2, y + l2 / 2, t + h / 2)

		k4 = h * f(x + k3, y + l3, t + h)
		l4 = h * g(x + k3, y + l3, t + h)

		#incremento de las variables dependientes (x, y)
		# y de la independiente (t)
		x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6
		y = y + (l1 + 2 * l2 + 2 * l3 + l4) / 6
		t += h

		#los resultados son almacenados en una lista de elementos (t, x, y)
		tabla.append((t, x, y))

	return tabla