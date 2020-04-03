def menu():
	print("""
1[+]Add patient.
2[+]Serving the first intern on the list.
3[+]Exit program.
	""")

class Wait:
	def __init__(self, choose):
		menu()
		self.choose = int(input("Select one option > "))
		self.cola = []
		self.name = ["HEllo", "World"]
		self.number = [8, 45]

	def add(self):
		if self.choose == 1:
			string='	'
			for x in self.name:
				for y in self.number:
					self.cola.append(string[x][y])
			return string
			
obj = Wait("")
print(obj.add())
