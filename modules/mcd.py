def mcd(a, b):
	resto = 0

	while a > 0:
		resto = a
		a = a%b
		b = resto
	return b

