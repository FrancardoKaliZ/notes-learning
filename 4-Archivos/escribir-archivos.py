txt_data = "Texto a agregar al archivo"

file_path = "4-Archivos/salida.txt"

with open(file = file_path, mode = "w") as file: #Se abre el archivo y se cierra con el "with" (devuelve un objeto archivo). La letra indica la accion para el archivo. Si no existe se crea
    file.write(txt_data)
    print(f"txt file '{file_path} se creo!")

#Con "x" escribiremos un archivo solamente si ese archivo no existe. Se reemplaza "x" en mode = " "