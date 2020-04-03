#-------------------------------------------------------------
# Modulo vectores
#--------------------------------------------------------------
# Proporciona constantes y funciones para el calculo vectorial en 3 dimensiones
#--------------------------------------------------------------
# Constante que exporta
#--------------------------------------------------------------
# vI, vJ, vK: vectores unidad
#
# Funciones que exporta
# vLeeVector:
# sin parametros
# devuelve un vector leido de teclado que se pide al usuario
#
# vMuestraVector
# muestra por pantalla el vector v con la notacion(x,y,z)
# no devuelve nada
#
# vLongitud(v):
# devuelve la longitud del vector v
#
# vSuma(u, v):
# devuelve el vecctor resultante de sumar u y v
#
# vProductoEscalar(u, v):
# devuelve el escalar resultante del producto escalar de u por v
#
# vProductoVectorial(u, v):
# devuelve el vector resultante del producto vectorial de u por v
#
# vSonPerpendiculares(u, v):
# devuelve cierto si u y v son perpendiculares, y falso en caso contrario
#----------------------------------------------------------------

# Funciones matematicas utilizadas


from math import sqrt

# Constantes

vI = [1, 0, 0]
vJ = [0, 1, 0]
vK = [0, 0, 1]

# Funciones de entrada y salida

def vLeerVector():
	x = float(input("Componente x: "))
	y = float(input("Componente y: "))
	z = float(input("Componente z: "))

def vMuestraVector(v):
	print("{0}, {1}, {2}".format(v[0], v[1], v[2]))

# Muestra calculo

def vSum(u, v):
	return [u[0]+v[0], u[1]+v[1], u[2]+v[2]]

def vLongitud(v):
	return sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def vProductoEscalar(u, v):
	return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def vSonPerpendiculares(u, v):
	return vProductoEscalar(u, v) == 0

def vProductoVectorial(u, v):
	resultado_x = u[1]*v[2] - u[2]*v[1]
	resultado_y = u[2]*v[0] - u[0]*v[2]
	resultado_z = u[0]*v[1] - u[1]*v[0]
	return [resultado_x, resultado_y, resultado_z]

