def inverliste(n):
	for i in range(len(n)//2):
		c = n[i]
		n[i] = n[len(n)-1-i]
		n[len(n)-1-i] = c
	return n

