import math

def one_third_simpson(a, b, f, n):
	h = (b - a) / n
	result = f(a) + f(b)
	x = a
	for i in range(1, n):
		x += h
		if i % 2 == 0:
			result += 2 * f(x)
		else:
			result += 4 * f(x)

	return (h / 3) * result

def f(x):
	return math.log(x)

n = 4
print '%s \t %.5f' % (n, one_third_simpson(1.0, 5.0, f, n))
