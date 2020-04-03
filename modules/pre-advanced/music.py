import pickle

class mp3:
	def __init__(self, titulo, interprete, duracion, estilo):
		self.titulo = titulo
		self.interprete = interprete
		self.duracion = duracion
		self.estilo = estilo

	def resumen(self):
		print("Titulo: {0}; Interprete: {1}".format(self.titulo, self.interprete))

	"""def options(self):
		print(
			[a+] Do you wanna add a new song?
			[b+] List all the songs of a certain artist
			[c+] List all the songs of a certain style
			[d+] List all songs in the database
			[e+] Delete a song from the database given the interpreter and title
			)
		choose = input("Select one option: ")

	def añadir(self):
		pass"""

	def __str__(self):
		string = ""
		string = string+"\nTitulo: {0}".format(self.titulo)
		string = string+"\nInterprete: {0}".format(self.interprete)
		string = string+"\nDuracion: {0}".format(self.duracion)
		string = string+"\nestilo: {0}".format(self.estilo)
		return string

music1 = mp3("Te quiero", "Juan Luis Guerra", 0.56, "Balada")
music2 = mp3("Hello", "Adele", 1.55, "Pop")
music3 = mp3("Perfect", "Ed Sheeran", 3.55, "Pop")
music4 = mp3("Me vas a extrañar", "Yiyo Sarante",3.40, "Salsa")
music5 = mp3("All of me", "Jhon Legend", 2.55, "Pop")
music6 = mp3("Love Me", "Jhon Legend", 3.56, "Pop")
al = ["music1", "music2", "music3", "music4", "music5", "music6"]

print(music1)

#guardar archivos & imprimo las canciones
def Sp():
	for element in al:
		print(element+" SAVED")
		arch1 = mp3
		fichero = open(element+".pickle", "wb")
		pickle.dump(element, fichero)
		fichero.close()
Sp()
