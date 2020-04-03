def escuadrada(filas, columnas):
	m = []
	for i in range(filas):
		m.append([0]*columnas)
		
	if len(m) == len(m[0]):
		return True
	else:
		return False
