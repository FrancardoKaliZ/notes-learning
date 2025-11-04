#Magic Methods  = Son metodos con doble guion bajo (__init__. __str__, __eq__, etc)
#Son creados de manera automatica por muchos buiilt ins de python
#Permite a los desarrolladores a definir y customizar el comportamientod de los objetos.
#Normalmente sirve para poder interactuar entre objetos eligiendo que parametros usar

class Libro:
    
    def __init__(self,titulo,num_paginas):
        self.titulo  = titulo
        self.num_paginas = num_paginas
    
    def __str__(self): #Cambia lo que devuelve el print de un objeto libro a lo q yo quiera de tipo string.( Normalmente devuelve el espacio de memoria )
        return f"{self.titulo} con {self.num_paginas} páginas!"

    def __eq__(self, other): #Es para ver si 2 objetos son iguales por parametros elegidos por mi. Devuelve booleano
        return self.titulo == other.titulo and self.num_paginas == other.num_paginas

    def __lt__(self,other): #Es para ver si algo es menos que otra cosa. Devuelve booleano
        return self.num_paginas < other.num_paginas
    
    def __gt__(self,other): #Es para ver si algo es mas que otra cosa. Devuelve booleano
        return self.num_paginas > other.num_paginas

    def __add__(self,other): #Para unir o sumar dependiendo el tipo de variable
        return self.num_paginas + other.num_paginas
    
    def __contains__(self,palabra): #Para ver si un valor se encuentra en un parametro. Devuelve booleano
        return palabra in self.titulo
    
    def __getitem__(self, key): #Sirve para poder acceder a un determinado atributo del objeto usando el nombre del atributo como "key"
        if key == "titulo":
            return self.titulo
        elif key == "num_paginas":
            return self.num_paginas
        else:
            return f"el atributo {key} no fue encontrado"
    
libro1=Libro("El señor de los anillos", 300)
libro2 = Libro("Harry Potter", 223)
print(libro1)
print(libro1 == libro2)
print(libro2 < libro1)
print(libro2 > libro1)
print(libro1+libro2)
print(libro1['titulo'])

