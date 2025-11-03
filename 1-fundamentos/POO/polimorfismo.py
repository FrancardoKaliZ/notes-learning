#El polimorfismo se puede conseguir de 2 maneras:
#Herencia y ducktyping

#Ejemplo de herencia

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #--> Esto significa que todas las clases que hereden de animal DIRECTAMENTE deben tener un metodo llamado comer, no importa como.(pueden ser distintos metodos para cada clase)
    # Pero las q lo heredan de multinivel no necesitan definirlo ya que lo heredan de la que lo hace directamente de "Animal"
    def comer(self):
        pass

class Perro(Animal):
    def __init__(self,nombre):
        self.nombre = nombre
    
    def comer(self):
        print(f"{self.nombre} esta comiendo!! ")
        
class Bulldog(Perro):
    def __init__(self,nombre, castrado):
        super().__init__(nombre)
        self.castrado = castrado

