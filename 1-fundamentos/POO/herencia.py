#La herencia es una manera de extender el codigo de una clase a otras.
#Existen distintos niveles de herencia, generando una "Escalera" entre las distintas clase padre e hijas, haciendo como una cadena de edad.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.esta_vivo = True

    def dormir(self):
        print(f"{self.nombre} está durmiendo!")

class Gato(Animal):
      def hablar():
        print("Maiw")

class Rata(Animal):
    def hablar():
        print("???")
    
gato1=Gato("Firualais")
rata1 = Rata("001")
gato1.hablar()
rata1.hablar()
rata1.dormir()
#El caso anterior fue de una herencia simple, donde una clase sub hereda atributos y metodos de la clase supper.
#Se puede heredar de infintas clases, es tan simple como solamente indicar de cuales quiero traer los metodos y atributos de la siguiente manera: C (A,B,"ETC") donde C es la calse hija y todo lo de adentro del partentesis son clases padre.
#Como se dijo anteriormente se puede tmb hacer una "cadena" de herencias de la siguiente manera:
#--> A → B(A) → C(B)
#(clase abuela) → (clase padre(clase abuela)) → (clase hija(clase padre))
