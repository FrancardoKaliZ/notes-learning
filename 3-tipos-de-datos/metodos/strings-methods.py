#Existe funciones y metodos para las cadenas, que devolveran una informacion que a futuro capaz nos pueda servir.
#Hay que tener en cuenta que siempre la cuenta para los "index", la posicion de algo, se empieza desde 0

oracion = input("Escribi tu oracion")

#Esto nos devuelve la longitud de caracteres del texto escrito, devuelve un INT
len(oracion)

#Devuelve la posicion en manera de numero, de la primera vez que aparece lo que pedimos
#En caso de no encontrar lo que pedimos, devuelve -1
result = oracion.find("LO QUE QUIERAS")

#Devuelve la posicion en manera de numero, de la ultima vez que aparece lo que pedimos
#En caso de no encontrar lo que pedimos, devuelve -1
result = oracion.rfind("LO QUE QUIERAS")

#Este metodo lo que hace es devolver un string con su primer index en mayuscula ( en caso de que no lo tenga )
Oracion = oracion.capitalize()

#Para transformar todas las letras en mayuscula
oracion = oracion.upper()
#Para transformar todas las letras en minusuclas
oracion = oracion.lower()

#Devuelve true o false, en caso de que solo sean digitos ( numeros ) devuelve true.
resultado1 = oracion.isdigit()

#Devuelve true o false, en caso de que solo sean caracteres alfabeticos, es decir letras ( sin incluir espacios o signos )
resultado2 = oracion.isalpha()

#Cuenta la cantidad de veces que aparece lo buscado en el ( ). Devuelve un Integer
resultado3 = oracion.count("a")

#ES DE LOS METODOS MAS UTILES Y USADOS. Sirve para reeplazar X por Y en todos lados de la oracion
oracion.replace("x", "y") #en Y podria dejar espacio vacio para sacar, por ejemplo, espacios

