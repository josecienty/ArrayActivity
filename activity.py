#create a programm to calculate array - crear un programa de calculo de matrices
#Dimension of an array - dimencion de la matriz
m=int(input("Especificar el numero de filas: ")) #number of rows
n=int(input("Especificar el numero de columnas: ")) #number of columnas

#our create a array null - creamos una matriz nula
M=[] #null, 0 elements
for i in range(m):
	M.append([0]*n)

#read numbers of keyboard
for i in range(m):
	for j in range(n):
		M[i][j]=float(input('Escriba el componente (%d, %d): '%(i,j)))
