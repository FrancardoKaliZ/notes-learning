#     --> Hace algo sí cumple la condición, y sino hace otra cosa, como "default" siempre va a hacer el else. Se pueden agregar infinitas condiciones a chekeear
edad = int(input("Ingrese su edad"))
adultez = int(input("Defina desde que edad empieza la adultez en su país"))

if edad>=adultez :
	print("Usted es un adulto")
elif edad<0 :
	print("Usted no nacio todavia!")
else:
	print("Usted todavia no es adulto")

#Se pueden poner infinitas condiciones en cada if, como tambien se pueden poner distintos flujos dentro de otros flujos(if / else dentro de un if )

#Para los booleanos se puede poner directamente la variable como condicion.

booleano = True
if booleano :
	print("El booleano es verdadero!")
else:
	print("El booleano es falso!")

#Existe otra manera mas "Rapida" en caso de que la condicion sea corta o entre dos valores. A esto se le llama "Operador Ternario"
# Sirve para usarlo en una sola linea de codigo, su formula general es:

condicion = True
vairable = "valor A" if (condicion) else "valor B"
print(vairable)


