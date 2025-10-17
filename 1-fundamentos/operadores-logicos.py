#Operadores logicos!!!
#     --> Sirven para evaluar mas de una condicion en un mismo control de flujo, existe el "or", "and", y el "not".

#En este caso necesito que ambas condiciones se cumplan en el primer if.
numero = 12
es_par = False
if numero % 2 == 0 and numero>10:
    print("El numero es par y mayor a 10")
elif numero % 2 == 0:
    print("El numero es solo par")
elif numero>10:
    print("El numero es solo mayor a 10")
else:
    print("El numero no es ni par ni mayor a 10")

#En este caso con que una de las dos condiciones se cumpla ya es suficiente para que suceda el primer condicional.
edad = 17
dia = "sabado"
if edad < 18 or dia == "sabado":
    print("Es muy joven para salir hoy!!!")
else:
    print("Que se divierta de joda!")

#En este caso pido que para que suceda mi condicional, pase el opuesto a su valor.
lloviendo = True
if not lloviendo:
    print("Es posible jugar el partido de futbol")
else :
    print("No es posible jugar el partido debido a la lluvia")



