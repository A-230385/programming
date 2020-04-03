#Este programa determina cual es el numero maximo de cinco numeros dados

def maximocandidato(a, b, c, d, e):
	candidato = a

	if b > candidato:
		maximo = b
	if c > candidato:
		maximo = c
	if d > candidato:
		maximo = d
	if e > candidato:
		maximo = e
	print('El maximo es:',maximo)
