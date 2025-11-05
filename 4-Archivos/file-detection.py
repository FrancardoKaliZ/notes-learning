import os #operating system
#Existen 2 tipos de paths para abrir archivos
#Relativo = carpeta/archivo.tipo
#Absoluto = C:/Users/Nombre/Desktop/archivo.tipo

file_path = "4-Archivos/text.txt"

if os.path.exists(file_path): # Devuelve true o false si existe
    print(f"El archivo existe en el lugar '{file_path}'")
    if os.path.isfile(file_path): # Sirve para checkear que el archivo sea un archivo y no un directory ( carpeta )
        print("Es un archivo")
    elif os.path.isdir(file_path):
        print("Es una carpeta")
else:
    print("No existe ese archivo")