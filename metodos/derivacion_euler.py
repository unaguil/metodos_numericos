import math
from matplotlib import pyplot
from matplotlib.ticker import MultipleLocator

def euler(h, n, f, x_0, y_0):
	y = y_0
	x = x_0
	for i in range(n + 1):
		f_val = f(x, y)
		hf = h * f_val
		print '%.1f \t %.5f \t %.5f \t %.5f' % (x, y, f_val, hf)

		y = y + hf
		x += h

def euler_mod(h, n, f, x_0, y_0):
	y = y_0
	x = x_0

	x_values = [x]
	y_values = [y]

	for i in range(n + 1):
		f_val = f(x, y)
		hf = h * f_val
		y_p = y + hf
		x_p = x + h
		f_p = f(x_p, y_p)
		f_m = 1/2.0 * (f_val + f_p)
		hfm = h * f_m
		y_a = y + hfm
		print '%.1f \t %.4f \t %.4f \t %.4f \t %.4f \t %.4f \t %.4f \t %.4f \t %.4f' % (x, y, f_val, hf, y_p, f_p, f_m, hfm, y_a)
		x = x_p
		y = y_a

		x_values.append(x)
		y_values.append(y)

	return x_values, y_values

def df_dx(x, y):
	return y * math.cos(x + y)

#print 'Metodo de Euler'
#euler(0.1, 4, df_dx, 0.0, -1.0)

print 'Metodo de Euler Modificado'
x_values, y_values = euler_mod(0.1, 200, df_dx, 0.0, 1.0)

minorLocator = MultipleLocator(1)

pyplot.plot(x_values, y_values)
pyplot.xlabel('t')
pyplot.ylabel('y(t)')
pyplot.axes().xaxis.set_minor_locator(minorLocator)
pyplot.grid(True)

pyplot.show()