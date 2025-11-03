#Class methods!!!
#     --> Son metodos para las clases en si. Toman a la clase como primer paramaetro

class Estudiante :

    contador = 0
    suma_notas = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        Estudiante.contador += 1
        Estudiante.suma_notas += nota

    #INSTANCE METHOD
    def get_informacion(self):
        return f"{self.nombre} , {self.nota}"
    
    @classmethod
    def get_contador(cls):
        return f"El total de estudiantes es : {cls.contador}"
    
    @classmethod
    def calcular_promedio(cls):
        if cls.count == 0:
            return 0
        else : 
            return f"{cls.suma_notas / cls.contador}" 
        
    
est1 = Estudiante("Mario", 8)
est2 = Estudiante("Josefina", 2)

print(Estudiante.get_contador())
print(Estudiante.calcular_promedio())