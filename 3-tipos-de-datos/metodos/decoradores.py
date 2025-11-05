#Sin argumentos 
def agregar_topping(func):
      def wrapper():
           print("Agregaste un topping")
           func()
      return wrapper

@agregar_topping
def get_helado():
     print("Aca está tu helado")


get_helado()

#Con argumentos

def agregar_topping(func):
      def wrapper(*args,**kwargs):
           print("Agregaste un topping")
           func(*args,**kwargs)
      return wrapper

@agregar_topping
def get_helado(sabor):
     print(f"Aca está tu helado sabor {sabor} ")

get_helado("chocolate")
