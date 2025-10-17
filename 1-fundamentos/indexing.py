#Sirve para acceder a elementos de una secuencia usando [] (indexing operator) [empieza : termina : paso :]
x = 0
y = 1
numeros_oracion = "184992416"
print(numeros_oracion[1]) #Muestra la posicion 1
print(numeros_oracion[x : y]) #Muestra hasta de X a Y ( donde X e Y son numeros ). En caso de que X lo dejes vacio lo toma como 0
print(numeros_oracion[x:]) #Muestra desde x en adelante, hasta el ultimo espacio de la secuencia.
print(numeros_oracion[-x]) #Muestra la posicion empezando desde el final, es decir en contando las posiciones de derecha a izquierda.
print(numeros_oracion[::2]) #Muestra cada 2 caracteres de mi string, va moviendose de 2 en 2
print(numeros_oracion[::-1]) #Invierte la cadena, es decir de "184992416" pasaria a "614299481"
