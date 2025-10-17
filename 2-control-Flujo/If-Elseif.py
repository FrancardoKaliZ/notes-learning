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





