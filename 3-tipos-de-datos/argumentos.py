#default arguments!!!
#    --> Son ciertos parametros que tienen un valor default cuando se omite. Permite que la funcion sea mas flexioble y reduce el numero de argumentos a usar.
# 1.POSICIONALES(en funciones)  2. DEFAULT  3.KEYWORD  4.ARBITRARIOS

def precio_neto(precio_lista,descuento = 0,impuesto = 0.5):
    return precio_lista * (1-descuento) * (1+impuesto)

print(precio_neto(250)) #--> Puedo mandar 1 argumento( el unico que no tiene el valor default ) o 2 argumentos, o los 3. 

import time

def contador (fin, inicio = 0): #Los argumentos default van al final o, mejor dicho, luego de los que si se les indica valor.
    for x in range(inicio, fin+1):
        print(x)
        time.sleep(1)
    print("Termino")

contador(7)

#keyword argument!!!
#    --> Es un argumento que le precede un identificador, ayuda para leer la funcion, no importa el orden de los argumentos.

def saludo(saludo,titulo,nombre,apellido):
    print(f"{saludo} {titulo} {nombre} {apellido}")

saludo("Hola", titulo = "Señor", apellido="Fernandez", nombre = "Juan") #Igual que en los defaul, los argumentos de posicion van primero, y luego el orden de los keyword arguments no importa.

#mini extra
print("1","2","3", sep="-") #Es un separador del mismisimo print!. Sirve para indicar como separar los valores a la hora de mostrarlos.

for x in range(0,20):
    print (x, end=" ") #En vez de crear una nueva linea ( default del print ) le indicamos que hacer en el end.

#Argumentos arbitrarios!!!
#    --> Existen 2 tipos. *args =  Permite pasar multiple non-key arguments y se crea una tupla.  **kwargs = Permite pasar multiple keyword arguments y se crea un diccionario. Se utiliza * para crearlos.

def sumar(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sumar(1,5,7,7)) # Puedo pasar la cantidad de argumentos que quiera, a la funcion llegaran como una tupla.

def mostrar_direccion(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    

mostrar_direccion(calle = "Rivadavia", #El orden no importa, pero si se mostrara como los pase y se creara el diccionario de esa manera.
                  ciudad= "BSAS",
                  zona = "Caballito",
                  num = "5126")

 #En caso de combinar en una funcion tanto args, como kwargs, el orden debera ser primero los de posicion ( args ) y luego los de key ( kwargs )
