def retirar_dinero(balance):
    dinero = float(input(f"Ingrese cuánto dinero va a retirar(cuenta con {balance}): "))

    if dinero < 0:
        print("No puede retirar menos de 0 pesos!!")
        return 0
    elif dinero > balance:
        print("No puede retirar más plata de la que tiene en su cuenta!")
        return 0
    else:
        return dinero


def ingresar_dinero():
    print("***************************************")
    dinero = float(input("Ingrese cuánto dinero quiere ingresar: "))
    print("***************************************")

    if dinero < 0:
        print("No puede ingresar menos de 0 pesos!!")
        return 0
    else:
        return dinero


def ver_balance(balance):
    print("***************************************")
    print(f"Tu dinero en cuenta es: ${balance:.2f}")
    print("***************************************")


def main():
    seguir = True
    print("***************************************")
    balance = float(input("Ingrese cuánto dinero hay en su cuenta: "))
    print("***************************************")

    while seguir:
        print("***************************************")
        print("Bienvenido al programa bancario")
        print("***************************************")
        print("1 - Ver dinero en cuenta")
        print("2 - Ingresar dinero en la cuenta")
        print("3 - Retirar dinero de la cuenta")
        print("4 - Salir del programa")

        eleccion = input("Ingrese su opción (1 - 4): ")

        if eleccion == "1":
            ver_balance(balance)
        elif eleccion == "2":
            balance += ingresar_dinero()
        elif eleccion == "3":
            balance -= retirar_dinero(balance)
        elif eleccion == "4":
            print("Nos vemos!")
            seguir = False
        else:
            print("No ingresó una opción válida")


if __name__ == '__main__':
    main()
