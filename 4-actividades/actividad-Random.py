import random

minimo = 1
maximo = 55
numero = random.randint(minimo,maximo) #--> De que valor a que valor se elije el numero random.
x = random.random() #--> Devuelve un numero random tipo float entre 0 y 1

opciones = ("Piedra", "papel", "tijeras")
opcion = random.choice(opciones)

cartas = ["2","3","4","5","6","7","8","Q","K","A"]
mezcladas = random.shuffle(cartas) #--> Reorganiza los valores de manera aleatoria.

import random
#juego numeros --> Comentar lo demas
menor_num = 1
mayor_num = 100
respuesta = random.randint(menor_num,mayor_num)
adivinanzas = 0
adivino = False

print("Bienvenido al juego de adivinar un numero!")
print(f"Elige un numero entre {menor_num} y {mayor_num}")

while not adivino:
    eleccion = input("Ingresa un numero: " )
    if eleccion.isdigit() :
        eleccion = int(eleccion)
        adivinanzas +=1
        if eleccion < menor_num or eleccion > mayor_num:
            print(f"El numero es demasiado grande, elija un numero entr {menor_num} y {mayor_num}" )
        elif eleccion < respuesta :
            print("El numero es mas grande!")
        elif eleccion > respuesta :
            print("El numero es mas chico!")
        else:
            print(f"Correcto, la respuesta era {respuesta}")
            print(f"Le tomo un total de {adivinanzas} intentos!")
            adivino = True

    else:
        print("Invalido, ingrese un valor numerico")


import random
#JUEGO PIEDRA PAPEL O TIJERAS  --> Comentar lo demas


contador_victorias =0
contador_derrotas =0 
contador_empates = 0
opciones1 = ("PIEDRA", "PAPEL", "TIJERAS")
continuar = True
while continuar :
    jugador = input(f"Elija su opcion :").upper()
    computadora = random.choice(opciones1)
    while jugador not in opciones1 :
        print("Eligio de manera invalida")
        jugador = input("Elija su opcion nuevamente: ").upper()
    print(f"El jugdor eligio : {jugador}")
    print(f"La maquina eligio : {computadora}")  
    if jugador == computadora:
        contador_empates +=1
        print(f"Sucedio un empate de {jugador}s")
    elif (jugador == "PIEDRA" and computadora == "TIJERAS") or (jugador == "PAPEL" and computadora == "PIEDRA") or (jugador == "TIJERAS" and computadora == "PAPEL"):
        contador_victorias +=1
        print(f"El jugador le gano a la computadora!!! {jugador} mata {computadora}")
    else :
        contador_derrotas +=1
        print(f"El jugador perdio! {computadora} mata {jugador}")
    print("desea continuar jugando?")
    seguir = input("Escriba 'Si' o 'NO' : ").upper()
    while seguir != "SI" and seguir != "NO" :
        if not seguir.isalpha() :
            seguir = input("Invalido, nada de cosas raras,  ingrese 'si' o 'no' unicamente: ").upper()
        else :
            seguir = input("Invalido, ingrese 'si' o 'no' unicamente: ").upper()
    if seguir == "SI":
        continuar = True
    elif seguir == "NO":
        continuar = False
        print("Abandono el juego!")
        print(f"Se retiro con --> victorias : {contador_victorias}, derrotas: {contador_derrotas} y empates: {contador_empates}")
minimo = 1
maximo = 55
numero = random.randint(minimo,maximo) #--> De que valor a que valor se elije el numero random.
x = random.random() #--> Devuelve un numero random tipo float entre 0 y 1

opciones = ("Piedra", "papel", "tijeras")
opcion = random.choice(opciones)

cartas = ["2","3","4","5","6","7","8","Q","K","A"]
mezcladas = random.shuffle(cartas) #--> Reorganiza los valores de manera aleatoria.
