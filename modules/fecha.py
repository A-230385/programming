class Fecha:
	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year

	def formato_largo(self):
		m = "mayo"
		return "\n{0} de {1} de {2}".format(self.day, m, self.year)

	def bisiest_year(self):
		return '\n',self.year%4 == 0 and (self.year%100 != 0 or self.year%400 == 0)

	def __str__(self):
		return "{0}/{1}/{2}".format(self.day, self.month, self.year)

obj = Fecha(24, 3, 2020)
print(obj, obj.formato_largo(), obj.bisiest_year())

