import math


print("Comenzando con python")
#Variables!!!
#     --> Dentro de las variables guardamos valores. Existen 4 ( string, integer, float y boolean)
#String
variableS = "Hola"
#Integer
variableI =  20
#Float ( a diferencia de int permite numeros con ",")
variableF = 15.2
#Boolean ( Puede ser o True O False NADA MAS! --> La primera letra en mayuscula para el valor.)
variableB = True

#TypeCasting!!!
#     -->  Es la manera para convertir un tipo de variable a otro
#Muestra el tipo de variable seleccionada.
print(type(variableS))
variableI = float(variableI)
variableF = str(variableF) #Luego de esto mi float pasa a ser un string, asi que debo tratarlo como tal.
#En caso de usar la transformacion de una variable a booleano, si la variable NO esta vacia, siempre devolvera "True", en caso de que si este vacia devolvera "False"
variableS = bool(variableS)
print(variableS)

#Input!!!
#     --> Es la manera para que el usuario ingrese data. Lo devuelve como string
entrada = input("Digite algo: ") #Si solo uso input siempre sera tratado como string.
numero = int(input("Digite un NUMERO: ")) #Hace el Typecast directamente a la hora de ingresar el dato. De esta manera ya lo convertimos en int y lo podemos usar como tal.

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
