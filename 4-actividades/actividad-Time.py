import time

#Mini app de contador.
mi_tiempo = int(input("Ingrese su tiempo en segundos: "))

for x in range(0,mi_tiempo+1) :
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1) #--> Cada cuanto tiempo se hace el conteo.
