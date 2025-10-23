#funciones!!!
#    --> Es un pedazo de codigo que es reutilizable. Para crear una funcion usamos () luego del nombre.
#En este caso veremos funciones con argumentos de posicion.

def feliz_cumpleaños():
    print("Feliz cumpleaños")
    print("Sos mas viejo!")

feliz_cumpleaños()

def ejemplo1(nombre): #--> Es importante saber que si yo paso data ( argumentos ) a la funcion, coincida en su llamado y en su creacion la cantidad de argumentos
    print(f"hola {nombre}")

ejemplo1("Matias") #--> Paso el argumento de tipo de variable que yo quiera, y en la creacion de la funcion le doy un nombre para cada argumento. 

def mostrar_datos(nombre,dni,fecha_naciemiento):
    print(f"Informacion de {nombre}")
    print(f"Cuyo DNI es : {dni}")
    print(f"Y nacio en la fecha : {fecha_naciemiento}")

mostrar_datos("Marisa",24269144,"20/3/1975")

#return!!!
#     --> El return es un sirve para finalizar la funcion y devolver un algo a donde se llama la funcion.

def sumar_nums(x,y):
    z = x+y
    return z

resultado = sumar_nums(2,6)
print(resultado)

def restar_nums(x,y):
    z = x-y
    return z
resultado2 = restar_nums(5,2)
print(resultado2)

def multiplicar_nums(x,y):
    z = x * y
    return z
resultado3 = multiplicar_nums(2,6)
print(resultado3)

def dividir_nums(x,y):
    z = x / y
    return z
resultado4 = dividir_nums(2,6)
print(resultado4)