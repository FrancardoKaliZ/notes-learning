#Exceptions
#       !!! Las exceptions son eventos que interrrumpen el flujo del programa dependiendo una situacion error de consola. Sirve para manejar dicho error y hacer que no se corte el run.
#(ZeroDivisionErro)(TypeError)(ValueError)

try:
    numero = int(input("Ingrese un numero: "))
    print(1/numero)
except ZeroDivisionError :
    print("No se puede dividir por cero")
except ValueError:
    print("Solo numero por favor!")
except Exception:
    print("Algo paso mal!")
finally:
    print("Limpiamos codigo o hacemos algo.")