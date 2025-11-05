import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars) #--> Lista de todos los caracteres
key = chars.copy()

random.shuffle(key) #-->Orden random

#ENCRIPTADO
texto = input("Ingresa que mensaje queres encriptar: ")
encriptado = ""

for letra in texto:
    index = chars.index(letra)
    encriptado += key[index]

print(f"Texto original: {texto}")
print(f"Texto encriptado: {encriptado}")

#DESENCRIPTADO
encriptado = input("Ingresa que mensaje queres desencriptar: ")
texto = ""

for letra in encriptado:
    index = key.index(letra)
    texto += chars[index]

print(f"Texto encriptado: {encriptado}")
print(f"Texto original( desencriptado ): {texto}")
