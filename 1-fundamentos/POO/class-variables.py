#Ejemplo en todo un mismo archivo, lo ideal seria un archivo de la clase maestro
class Maestro:

    class_año = 2025
    num_maestros = 0

    def __init__(self,nombre,edad,enseñando):
        self.nombre = nombre
        self.edad = edad
        self.enseñando = enseñando
        Maestro.num_maestros += 1 #Sumará 1 siempre que se cree un objeto maestro nuevo

    def castigar(self):
        print(f"Estas castigado en nombre de {self.nombre}")



maestro1 = Maestro("Juan", 20, True)
maestro2 = Maestro("Cinthya", 50, True)

maestro1.castigar()

print(f"Hay {Maestro.num_maestros} enseñando en el colegio en el año {Maestro.class_año}")


