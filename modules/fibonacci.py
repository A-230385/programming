def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	elif n > 2:
		print("Starting the fibonacci calculation of",n)
	return fibonacci(n-1)+fibonacci(n-2)

