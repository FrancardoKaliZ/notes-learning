# While!!!
#     --> Se usan para que se ejecute algo mientras la conidcion se cumpla ( puede ser de manera infinita ). La diferencia con el if es la cantidad de veces que corre la condicion.

nombre = input("Ingrese su nombre: ")
while nombre == "": #Se toma como en los if, esto es una condicion y en este caso siempre q sea verdadera pasara lo siguiente.
    print("No escribio nada.Ingrese su nombre por favor")
    nombre = input("Ingrese su nombre: ") # Si no se pondria esta linea de codigo, entraria a un loop infinito en caso de dejar el nombre vacio.
print(f"Hola, {nombre}")

#tambien se puede hacer de manera inversa, es decir que se ejecute de manera infinta hasta que suceda algo.

peli = input("Ingrese una pelicula que le guste muhco(ingrese q para salir): ")
while peli != "q": #tambien puedo poner not peli == "q"
    print(f"Te gusta la peli, {peli}")
    peli = input("Ingrese otra pelicula que le guste muhco: ")
print("chao")

#Puedo usar operadores logicos para las condiciones (../1-fundamentos/operadores-logicos.py )

# For!!!
#     --> Ejecuta un bloque de codigo un x cantidad de veces, el x lo puedo poner como numero literal, como una condicion o para tratar iteraciones.
# la formula dentro del range usa la misma logica que el indexing ( inicio , fin , paso )

for x in range(1,11): # En este caso el range sirve para ver de donde empiezo a donde termino, si no especifico el inicio, lo hace desde 0. Tener en cuenta que si quiero contar hasta x numero, el final debera ser x+1
    print(x)

for x in reversed((1,11,2)): # Va de x+1 hasta el inicio, cuenta de manera inversa de 2 en 2
    print(x)

#se puede trabajar con strings

cadena = "122235"
for x in cadena: #Muestra posicion a posicion
    print(x)

#Se puede "SKIPEAR" un valor de la cadena o del conteo si se desea
for x in range(1,22):
    if x == 20:
        continue # -->
    else:
        print(x)

#Se puede dar un valor en el que termine el recorrido de la cadena o del conteo si se desea
for x in range(1,22):
    if x == 20:
        break # -->
    else:
        print(x)