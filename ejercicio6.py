import os
import sys
def listin():
    print("----------------------------------------------------\n"
          "           Listado Telefonico                       \n"
          "----------------------------------------------------\n"
          "        1) Crear Listado Telefonico\n"
          "        2) Consulta\n"
          "        3) Añadir Nuevo Telefono\n"
          "        4) Eliminar Telefono\n"                   
          "        5) Salir\n"
          "----------------------------------------------------\n")
    opcion = int(input("Elige una opcion:\n"))
    if opcion == 1:
        crear_listado()
    elif opcion == 2:
        nombre = input("Introduzca el nombre del cliente que quiere consultar: \n")
        consulta(nombre)
    elif opcion == 3:
        nuevo_cliente = input("Introduzca el nombre del nuevo cliente: \n")
        nuevo_tel = input("Introduzca el nuevo numero de telefono: \n")
        new_telefono(nuevo_cliente, nuevo_tel)
    elif opcion == 4:
        del_tel = input("Introduzca el numero de telefono que desea eliminar: \n")
        eliminar_tel(del_tel)
    elif opcion == 5:
        sys.exit()
    else:

        print("Error, numero incorrecto")
    return

def crear_listado():
    if not os.path.isfile("N:\DAPI\practica0206_Rouidjali\listin.txt"):
        file = open("N:\DAPI\practica0206_Rouidjali\listin.txt", "w")
        file.close()
    return
def consulta(nombre):
    with open("N:\DAPI\practica0206_Rouidjali\listin.txt", "r") as file:
        lista = file.readlines()
        for lines in lista:
            if nombre in lines:
                print(lines)
    return
def new_telefono(nuevo_cliente, nuevo_tel):
    with open("N:\DAPI\practica0206_Rouidjali\listin.txt", "a") as file:
        texto = "\n" + nuevo_cliente + " , " + nuevo_tel
        file.write(str(texto))
    return
def eliminar_tel(del_tel):
    with open("N:\DAPI\practica0206_Rouidjali\listin.txt", "r") as file:
        lines = file.readlines()
    with open("N:\DAPI\practica0206_Rouidjali\listin.txt", "w") as files:
        for line in lines:
                if del_tel not in line.strip("\n"):
                    files.write(line)
    return
opcion = 0
while opcion != 5:
    listin()