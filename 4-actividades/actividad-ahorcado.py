import random
print("\n")
print("********************************")
print("********************************")
print("\n")
print("Bienvenido al juego del ahorcado.")
print("\n")
print("********************************")
print("********************************\n")


print("REGLAS:")
print("-> Un jugador elige una palabra y el otro trata de adivinarla letra a letra.")
print("-> Cada letra no acertada resta una vida (tienen 6 vidas).")
print("-> Si intenta adivinar la palabra completa y falla, pierde todas las vidas.")
print("-> Adivinar una palabra suma 3 puntos.")
print("-> Perder todas las vidas resta 1 punto.")
print("********************************")
print("********************************\n")

jugador1 = input("Ingrese el nombre del jugador 1: ")
puntosJ1 = 0
jugador2 = input("Ingrese el nombre del jugador 2: ")
puntosJ2 = 0

ahorcado = {
    0 : ("   ",
         "   ",
         "   ",),
    1 : (" o ",
         "   ",
         "   "),
    2 : (" o ",
         " |  ",
         "   "),
    3 : (" o ",
         "/|  ",
         "   "),
    4 : (" o ",
         "/|\\  ",
         "   "),
    5 : (" o ",
         "/|\\  ",
         "/   "),
    6 : (" o ",
         "/|\\  ",
         "/ \\   "),
}

opciones = ["1", "2", "3"]

def mostrar_pista(pista):
    print(" ".join(pista))

def mostrar_ahorcado(num):
    print("*********************")
    for linea in ahorcado[num]:
        print(linea)
    print("*********************")

def mostrar_resultados():
    print("\n")
    print("***** RESULTADOS *****")
    print(f"{jugador1}: {puntosJ1} puntos")
    print(f"{jugador2}: {puntosJ2} puntos")
    print("***********************\n")

def ronda(palabra, adivinador):
    vidas = 6
    letras_usadas = set()
    pista = ["_"] * len(palabra)

    while vidas > 0 and "_" in pista:
        mostrar_ahorcado(6 - vidas)
        mostrar_pista(pista)
        print(f"Letras usadas: {', '.join(sorted(letras_usadas))}")
        print(f"Vidas restantes: {vidas}")

        letra = input(f"{adivinador}, ingresa una letra: ").lower()
    #Hago 3 filtros para comprobar que este bien lo ingresado:

         # 1- intento de palabra completa
        if len(letra) == len(palabra):
            if letra == palabra:
                pista = list(palabra)
                break
            else:
                print("¡Palabra incorrecta! Perdiste todas las vidas.")
                vidas = 0
                break
         # 2- intento de escribir algo distinto a una letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una LETRA.")
            continue
         # 3- intento de repetir letra  
        if letra in letras_usadas:
            print("Ya usaste esa letra.")
            continue

        letras_usadas.add(letra)
        #Chekeo normal de q este dentro de la palabra a adivinar
        if letra in palabra:
            print("Acertaste una letra!")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    pista[i] = letra
        else:
            print("La letra no se encuentra en la palabra.")
            vidas -= 1

    mostrar_ahorcado(6 - vidas)
    mostrar_pista(pista)
    #Caso ganador
    if "_" not in pista:
        print(f"Felicidades {adivinador}! Adivinaste la palabra '{palabra}'.")
        return 3  
    #Caso perdedor
    else:
        print(f"{adivinador} perdió todas sus vidas! La palabra era '{palabra}'.")
        return -1  

def main():
    seguir = True
    global puntosJ1,puntosJ2 #Con esto uso las variables globales ( gracias chatgptx2 )
    while seguir:
        print("\n")
        print("********************************")
        print("\n")
        print(f"Opción 1 : {jugador1} elige la palabra y {jugador2} adivina")
        print(f"Opción 2 : {jugador2} elige la palabra y {jugador1} adivina")
        print("Opción 3 : Finalizar el juego")
        print("\n")
        print("********************************")

        eleccion = input("Ingrese '1', '2' o '3': ")

        while eleccion not in opciones:
            print("Opción inválida.")
            eleccion = input("Ingrese '1', '2' o '3': ")

        if eleccion == "1":
            palabra = input(f"{jugador1}, ingrese la palabra para que {jugador2} la adivine: ").lower()
            print("\n" * 50)  # --> limpia pantalla (GRACIAS CHATGPT)
            puntosJ2 += ronda(palabra, jugador2)

        elif eleccion == "2":
            palabra = input(f"{jugador2}, ingrese la palabra para que {jugador1} la adivine: ").lower()
            print("\n" * 50)
            puntosJ1 += ronda(palabra, jugador1)

        elif eleccion == "3":
            mostrar_resultados()
            seguir = False

if __name__ == '__main__':
    main()
