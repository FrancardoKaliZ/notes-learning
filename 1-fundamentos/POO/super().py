#Es una funcion usada en una clase hija para llamar metodos y atributos de la superclase. Es para no repetir codigo cuando varias clases coinciden en atributos y metodos.

class Forma():
    def __init__(self,color,esta_lleno):
        self.color = color
        self.esta_lleno = esta_lleno

    def describir(self):
        print(f"Es de color {self.color} y {'esta lleno' if self.esta_lleno else 'no esta lleno'}")

class Circulo(Forma):
    def __init__(self,color,esta_lleno,radio):
        super().__init__(color,esta_lleno)  
        self.radio = radio  
    
    def describir(self):
        print(f"Es un circulo con radio : {self.radio}cm ")
        super().describir()
  
class Triangulo(Forma):
    def __init__(self,color,esta_lleno,altura,lados):
        super().__init__(color,esta_lleno)  
        self.altura = altura
        self.lados = lados


class Rectangulo(Forma):
    def __init__(self,color,esta_lleno,base,altura):
        super().__init__(color,esta_lleno)  
        self.altura = altura
        self.base = base
