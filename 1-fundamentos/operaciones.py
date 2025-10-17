import math
#Operaciones Aritmeticas!!!
#     --> Las clasicas se encuentran en el archivo, aqui veremos las de codigo
x = 1.62
y = 4
z = -2
#Redondea el numero, si el ,>5 se tira para arriba, sino se tira para abajo
redondeo = round(x)
print(redondeo)
#Es el valor absoluto de un numero, siempre sera positivo
absoluto = abs(z)
print(absoluto)
#Es para la funcion exponencial, se elige primero la base y luego el exponente
expo = pow(x,y)
print(expo)
#Es para conseguir el numero maximo o minimo entre una seleccion de variables
maximo = max(x,y,z)
minimo = min(x,y,z)
#Con la importacion de math al principio del codigo podemos usar variable matematicas ya creadas.
print(math.pi)
print(math.e)
#Raiz cuadrada USANDO MATH
raiz = math.sqrt(y)
print(raiz)
#Para redondear si o si para arriba o si o si para abajo, si existe un decimal
arriba  = math.ceil(x)
abajo = math.floor(x)
print(arriba, abajo)
