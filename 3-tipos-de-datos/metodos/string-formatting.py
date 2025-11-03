# Es la manera en la q se edita una cadena de texto antes de mostrarla, pero sin cambiar su valor orignal.
# Su formula es {valor : flag } --> Donde la flag es la "edicion" a realizar.

numero = 21923.1452

print(f"Numero es: {numero:.2f}") # El .xf lo que hace es mostrar hasta x decimales
print(f"Numero es: {numero:9}") # El numero se mostrara en 9 espacios si o si, en este caso se rellenaria con espacios blancos previos al numero
print(f"Numero es: {numero:09}") # El numero se mostrara en 9 espacios si o si, en este caso se rellenaria con espacios con el valor 0 previos al numero
print(f"Numero es: {numero:<10}") # Estan "justificados por derecha", es decir todos los espacios en blanco iran al final del numero hasta ocupar 10 espacios.
print(f"Numero es: {numero:>10}") # Estan "justificados por izquierda", es decir todos los espacios en blanco iran al principio del numero hasta ocupar 10 espacios. Es el default
print(f"Numero es: {numero:^10}") # Estan "justificados en el centro", los espacios se diviran de mamnera equitativa entre antes del numero y al final del numero.
print(f"Numero es: {numero:+}") # Agrega el signo "+" previo a los numeros positivos y "-" a los numeros negativos. Se puede dejar un espacio en blanco y no mostrara el "+" pero si el "-" en los negativos
print(f"Numero es: {numero:,}") # Sirve para numeros mas grandes, separa todos las milesimos por comas.

# Se puede combinar en distintos conjuntos de flags, pero deben seguir un orden estricto ( buscarlo en google ). Ejemplo:
print(f"Numero es: {numero:<+10,.3f}")