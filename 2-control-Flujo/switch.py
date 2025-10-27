#Switch!!!
#     --> Una forma alterativa de usar muchos elif. Ejecuta algo de codigo si un valor matchea el caso. Es mas facul de leer la sintaxis y el codigo quda mas "LIMPIO".

def dia_semana(dia):
    match dia:
        case 1:
            return "Es domingo"
        case 2: 
            return "Es lunes"
        case 3: 
            return "Es martes"
        case 4: 
            return "Es miercoles"
        case 5: 
            return "Es jueves"
        case 6: 
            return "Es viernes"
        case 7: 
            return "Es sabado"
        case _:
            return "No es un dia valido"

print(dia_semana(4))
#Se puede poner cualquier tipo de valor en el case, depende lo que estemos buscando.

def es_finde(dia): #--> Uso el or " | " , para simplificar los casos y no repetirme en la sintaxis.
    match dia:
        case "Lunes" | "Martes" | "Miercoles" | " Jueves" | "Lunes":
            return False
        case "Sabado" | "Domingo":
            return True
        
print(es_finde("Sabado"))
        