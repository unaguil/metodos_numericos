import math

def sol_analitica():
	return 0.5 * (1 - 1/math.e)

def termino(t):
	x = (t + 1)
	return x * math.exp(-(x*x)/4.0)

def sol_numerica(n, t, p):
	total = 0.0
	for i in range(n):
		total += p[i] * termino(t[i])
 
 	return 0.25 * total

def error_relativo(aprox, real):
	return math.fabs((aprox - real) / real)

valores = {
		   1: ((0.0, ), (2.0, )),
		   2: ((-0.57735027, 0.57735027), (1.0, 1.0)),
		   3: ((-0.77459667, 0.0, -0.77459667), (0.55555555, 0.88888889, 0.55555555)),
		   4: ((-0.86113631, -0.33998104, 0.33998104, -0.86113631), (0.34785485, 0.65214515, 0.65214515, 0.34785485))
		   }

analitica = sol_analitica()
print "Valor analitico: %0.6f" % analitica
for n in valores.keys():
	numerica = sol_numerica(n, valores[n][0], valores[n][1])
	print "n=%i valor=%0.6f e=%0.6f" % (n, numerica, error_relativo(numerica, analitica))