
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
	for i in range(n + 1):
		f_val = f(x, y)
		hf = h * f_val
		y_p = y + hf
		x_p = x + h
		f_p = f(x_p, y_p)
		hf_p = h * f_p 
		y_a = y + h/2 * (f_val + f_p)
		print '%.1f \t %.5f \t %.4f \t %.4f \t %.4f \t %.4f' % (x, y, hf, y_p, hf_p, y_a)
		x = x_p
		y = y_a		 

def df_dx(x, y):
	return -2*x + - y

print 'Metodo de Euler'
euler(0.1, 4, df_dx, 0.0, -1.0)

print 'Metodo de Euler Modificado'
euler_mod(0.1, 4, df_dx, 0.0, -1.0)
