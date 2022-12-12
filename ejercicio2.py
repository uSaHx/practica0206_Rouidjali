import os
def leer_tabla(n):
    if n in range(1,11):
        nombre_archivo = "tabla-" + str(n) + ".txt"
        if os.path.isfile("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali/" + nombre_archivo):
            print("El archivo existe")
        else:
            print("El archivo no existe")
    return

leer_tabla(7)