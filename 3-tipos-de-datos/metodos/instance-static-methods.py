#Existen disntintos tipos de metodos. Los "Instance methods" que ya los conocemos y los "Static Methods"
#Los static methods es un metodo que pertenece a la clase mas que a un objeto de esa clase. No trabajamos con los objetos como en las de isntancia

class Empleado :
    def __init__(self,nombre,posicion):
        self.nombre = nombre
        self.posicion = posicion

    def get_infor(self): #-->Instance method
        return f"{self.nombre} = {self.posicion}"
    
    @staticmethod #--> No depende de ningun objeto en especifico para usar este metodo. Solamente tengo que llamarla de la clase en el main.
    def es_pos_valida(posicion):
        validados = ["Manager","Recepcionista","Cocinero"]
        return posicion in validados
    
print(Empleado.es_pos_valida("Cocinero"))
