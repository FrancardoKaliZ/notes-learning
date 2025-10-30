class Perro:
    def __init__(self,raza,edad,castrado):
        self.raza = raza
        self.edad = edad
        self.castrado = castrado

    def ladrar(self):
        print(f"WOOF WOOF! (en {self.raza})")