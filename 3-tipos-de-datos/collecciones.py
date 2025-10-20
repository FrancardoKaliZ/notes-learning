#Colecciones!!!
#     --> Son variables que tienen muchos valores
#Se puede usar todo el material de INDEXING en listas y tuplas
#Todas son iterables, se pueden usar controles de flujo

#Lista = [] --> Ordenada y cambiable, admite duplicados
index = 2
frutas = ["banana", "manzana", "sandia", "maracuya"] #--> Se puede entrar a cada elemento de manera individual indicando su index(pos)
help(frutas) #--> Me indica y explica todas las funciones y atributos que se pueden usar en las listas  
frutas.append("coco") #--> Agrega al FINAL de la lista el valor dado.
frutas.remove("valor") #--> Elimina el valor de la lista, SOLO la primer vez q aparece
frutas.insert(index,"valor") #--> Ingresa el valor en el lugar de la lista dado ( index ).
frutas.sort() #--> Se ordenan de manera alfabetica.
frutas.reverse() # --> Se ordenan en viceversa teniendo en cuenta su posicion. Su index
frutas.clear() #--> Elimina todos los elementos
frutas.index("manzana") #--> Devuelve la pos de la lista donde se encuentra el valor. Si no se encuentra tira error.
frutas.count("banana") #--> Cuenta la cantidad de veces que aparece el valor elegido en la lista. 

#Set = {} --> Desordenado e INMUTABLES(no se pueden cambiar sus valores).Podemos agregar/eliminar elementos, No se puede duplicar.
#No se puede usar INDEXING al estar desordenado.
nombres = {"Juan", "Pepe", "Rodrigo"}
help(nombres) #--> Misma logica que el help de la lista.
nombres.add("Pablo") #--> Agrega el valor DONDE SEA.
nombres.remove("valor") #--> Elimina el valor del set.
nombres.pop() #--> Saca el primer elemento, al ser random el orden uno no elige que saca.
nombres.clear() #--> Igual que en la lista.

#Tuplas = () --> Ordenadas y no se pueden cambiar(inmutables y no se puede eliminar/agregar). Se puede duplicar y son mas "rapidas"
ciudades = ("BSAS", "NY", "Las Vegas")
help(ciudades) #--> Misma logica de siempre
print("valor" in ciudades) #--> Devuelve true o false dependiendo si el valor se encuentra o no en la tupla
print(ciudades.index("NY")) #--> Devuelve la pos de la tupla donde se encuentra el valor. Si no se encuentra tira error.
print(ciudades.count("Las vegas")) #--> Cuenta la cantidad de veces que aparece el valor elegido en la tupla.


#Se pueden crear tuplas y listas 2D
#Basicamente son listas/tuplas que tienen como valores otras listas/tuplas. Se pueden combinar entre si
x, y = 1
lista_listas = [nombres, ciudades] #--> Se puede crear tambien directamente que en cada lista dentro de la lista, esten entre [los valores]
lista_listas[x][y] #--> Es la manera de entrara sapber el index de 1 elemento y en la lista x
#Dependiendo de cada item de la lista de listas, tendra las funciones y atributos disponibles para el tipo de colleccion.

#Diccionarios!!!
#     --> Tambien son un tipo de coleccion, pero vienen como pares ({key:value}). Esta ordenado y se puede cambiar, pero no se puede duplicar

capitales = {"Argentina" : "BSAS",
             "USA" : "Washington D.C",
             "China" : "Beijing"}
help(capitales)
capitales.get("key") #--> Escribirmos la key y buscamos su valor por la misma. Si no esta lo q escribimos en el diccionario, devuelve NONE
capitales.update({"Alemania" : "Berlin"}) #--> Agrega al final en caso de no existir, o se cambia el valor si existe la key.
capitales.pop("key") #--> Se puede eliminar un elemento utilizando la key
capitales.popitem() #--> Elimina el ultimo valor del diccionario.
capitales.clear() #-->Limpia el diccionario

keys = capitales.keys() #--> Agarra solo las keys, ya que tecnicamente es una lista de las mismas, pero con un valor con cada pos.Se explica mejor en POO
valores = capitales.values() #--> Lo mismo que lo de arriba, pero con los valores en vez de las keys

items = capitales.items() #--> Devuelve como conjunto de lista 2d los elementos, emparejados en (keys,values) como tuplas.