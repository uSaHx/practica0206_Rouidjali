def tabla_mutply(n):
    if n in range(1,11):
        nombre_archivo = "tabla-" + str(n) + ".txt"
        open("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali/" + nombre_archivo, "w")
        with open("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali/" + nombre_archivo, "w") as file:
            for x in range(1 ,11):
                mutiply = str(n) + "*" + str(x) + "=" + str((x*n)) + "\n"
                file.write(mutiply)
    return

tabla_mutply(7)