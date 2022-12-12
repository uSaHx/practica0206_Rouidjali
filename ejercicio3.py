import os
def busca_num(n, m):
    if n in range(1, 11):
        nombre_archivo = "tabla-" + str(n) + ".txt"
        if os.path.isfile("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali/" + nombre_archivo):
           with open("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali/" + nombre_archivo, "r") as file:
              mutilplies = file.readlines()
              for x in mutilplies:
                  if str(m in x:
                      print(x)
        else:
            print("El archivo no existe")
    return

busca_num(5, 7)