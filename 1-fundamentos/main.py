#if __name__ == __main__ : --> Las funciones y clases de este modulo pueden ser rehutilizadas sin que el bloque principal se este ejecutando. Se puede importar a otros archivos o runnearlo en el mismo( sirve a la hora de ejecutar distintos archivos)
#Normalmente lo utilzamos para extraer cosas de otros programas, funciones por ejemplo. Y normalmente cada programa tiene su propio archivo "main.py" que se crea de manera default.
#Siempre habra un arhivo "main", pero no se llamara asi si o si. Es el archivo que por default corre. De esta manera podemos diferenciar entre que programas o archivos correr.
#PARA ENTENDER MEJOR VER EL VIDEO "PYHTON FULL COURSE FOR FREE DE BRO CODE MINUTO: 5 HORAS 15 MINUTOS 35 SEGUNDOS."

def main():
    print("hola")

if __name__ == '__main__':
    main()

