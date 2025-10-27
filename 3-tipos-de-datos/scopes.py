#Variable scope
#     --> Donde una variable es visibel y accesible
#Scope Resolution
#     --> Existen 4 tipos de niveles: (LEGB). Local -> Enclosed -> Global -> Built-in. En este orden se hace la busqueda de valores para usarse.
#Las 

def func1():
    a=1 #La variable a es Local a la func1
    print(a)
    print(x)

def func2():
    b=2 #La variable b es Local a la func1
    print(b)
    print(x)
func1()
func2()
#Las enclosed son donde hay una funcion definida dentro de otra( se vera mas adelante ). Primero se busca la variable de manera local ( seria en la funcion definida dentro de la otra ), en caso de no encontrarse se busca en enclosed scope ( seria en la funcion principal )

#Es una variable de scope Global. En caso de tener una local, la funcion usara el valor de la variable local e "ignora" el valor de la global. Sino utiliza el valor de la global
x = 4
#En este caso estamos usando una variable de scope Built-in. Son las que se importan
from math import e
def func3():
    print(e)

e = 4
func3()
#IMPORTANTE --> Las variables pueden coincidir en nombre si su scope es distinto. En este caso el e importado tiene un valor (scope Built-in) y el e = 4(Global) otro, no estoy redifiniendo el e importado, pero por orden muestro el global.
