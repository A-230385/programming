class Cola:
	def __init__(self):
		self.cola = []

	def añade(self, elemento):
		self.cola.append(elemento)

	def primero(self):
		if len(self.cola) == 0:
			return None
		else:
			return self.cola[0]

	def sacaPrimero(self):
		if len(self.cola) > 0:
			del self.cola[0]

	def __str__(self):
		string = ""
		for elemento in self.cola:
			string = string+str(elemento)+" "
		return string

	def tamaño(self):
		return len(self.cola)

	def esVacia(self):
		return len(self.cola)==0

	def copia(self):
		new = Cola()
		return new

obj = Cola()
print(obj.añade(8), obj.primero(), obj)


