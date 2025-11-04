#@property
#     --> Es un decorador para definir a un metodo como una propiedad ( accesible como un atributo )
# Te permite utilizar el getter, setter u deleter method para los atributos.

class Rectangulo:
    def __init__(self,altura,base):
        self._altura = altura #Con un "_" luego del punto hacemos que los atributos sean privados. Eso significa que solo pueden ser accesibles por esta clase unicamente.
        self._base = base

    @property # Le pongo el nombre del atributo para "editar" lo que me muestre cuando acceda al mismo. Hago el chekeo tmb con manejo de errores por si no existe el atributo o se borro. "Getter"
    def altura(self):
        try:
            return f"{self._altura}cm"
        except AttributeError:
            return "(sin altura)"
        
    @property
    def base(self):
        try:
            return f"{self._base}cm"
        except AttributeError:
            return "(sin base)"
        
    @altura.setter # Con el setter sirve a la hora de darle un valor a al variabel con el "=". "Setter"
    def altura(self,nueva_altura):
        if nueva_altura > 0:
            self._altura = nueva_altura
        else:
            print("La altura debe ser un numero mayor a 0")

    @base.setter
    def base(self,nueva_base):
        if nueva_base > 0:
            self._base = nueva_base
        else:
            print("La base debe ser un numero mayor a 0")

    @altura.deleter #Elimino el atributo de la clase. "Deleter"
    def altura(self):
        del self._altura
        print("La altura fue borrada")

    @base.deleter
    def base(self):
        del self._base
        print("La base fue borrada")

    def __str__(self): 
        return f"rectangulo de altura {self.altura} con base {self.base}" #Utilizo los atributos del getter        
    
rectangulo1 = Rectangulo(4,6)
print(rectangulo1.altura)
rectangulo1.base = 22
del rectangulo1.altura
print(rectangulo1)