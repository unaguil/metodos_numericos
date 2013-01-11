import cmath

def tfd(x):
	N = len(x)
	espectro_freq = []
	for n in range(N):
		c = 0
		for k in range(N):
			c += x[k] * cmath.exp(-2j * cmath.pi * n * k / N)
		espectro_freq.append(c)

	return espectro_freq 
