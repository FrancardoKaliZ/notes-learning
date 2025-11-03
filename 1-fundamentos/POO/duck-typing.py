#Es otra manera de hacer polimorfismo:
#El objeto debe tener un minimo de atributos y metodos necesarios
#"Siempre que un objeto se parezca a otro, puede ser tratado como este otro."

class Animal:
    vivo = True

class Perro(Animal):
    def hablar(self):
        print("WOOF!")

class Gato(Animal):
    def hablar(self):
        print("MIAW!")

class Auto:
    vivo = False
    
    def hablar(self):
        print("HONK!")
        

animales = [Perro(), Gato(), Auto()] #--> Auto tiene el minimo metodo ( "HABLAR ") para ser considerado un "Animal"
for animal in animales:
    animal.hablar()
    print(animal.vivo)