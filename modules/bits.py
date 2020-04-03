def bits(n):
	if n == 0 or n == 1:
		result = 1
	else:
		result = 1+bits(n//2)
	return result

