#Programacion orientada a objetos!!!
#    --> El objeto es un conjunto de atributos(variables) y metodos(funciones) relacionados.
#    --> La clase es como el plano para diseñar la estructura de un objeto, es necesaria a la hora de crear uno.

class Auto:
    def __init__(self,modelo,año,color,disponible_venta):
        self.modelo = modelo
        self.color = color
        self.año = año
        self.disponible_venta = disponible_venta

auto1 = Auto("Chevrolet", 2017, "Azul", True) #Hay q pasar la misma cantidad de atributos, funciona igual que el tema de argumentos para funciones
#Para ingresar a algun atributo especifico, hacemos lo mismo que en los modulos.  

#Normalmente los objetos se encuentran o, en un mismo archivo python todos juntos, o cada uno con su propio archivo por separado.
#Se exportan al main ( este archivo en este caso ) y se utilizan sus metodos y se pueden crear desde aqui.

import sys
import os

# Obtiene la ruta del proyecto hasta 1-fundamentos
# Agrega la carpeta actual (POO) al path de búsqueda de módulos
# Debo hacer esto debido a mi estructura del proyecto entero ( ya que mis carpetas empiezan con numeros ). 

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_path)

from perro import Perro


perro1 = Perro("Buldog",7, True)
perro1.ladrar()
