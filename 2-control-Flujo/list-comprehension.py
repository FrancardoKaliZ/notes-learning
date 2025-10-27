#List comprehension!!!
#     --> Es una manera de crear listas en python, de manera mas compacta y sencilla que los loops tradicionales. Su estructura es: [expression for valor in iterable if condicion]

dobles = [x*2 for x in range(1,11)]
print(dobles)

#Se puede "saltear" un paso y creaar directamente la lista en la zona donde iria el iterable en la estructura.

numeros = [1,2,-5,-7,6] 
nums_positivos = [num for num in numeros if num>=0]
nums_negativos = [num for num in numeros if num<0]
print(nums_positivos)
print(nums_negativos)
