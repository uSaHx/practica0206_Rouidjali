import os
def listin():
    print("----------------------------------------------------"
          "           Listado Telefonico                       "
          "----------------------------------------------------"
          "        1) Crear Listado Telefonico"
          "        2) Consulta"
          "        3) Añadir Nuevo Telefono"
          "        4) Eliminar Telefono"                   
          "        5) Salir"
          "----------------------------------------------------")
    opcion = input("Elige una opcion:")
    if opcion == 1:
        crear_listado()
    if opcion == 2:
        consulta()
    if opcion == 3:
        nuevo_cliente = input("Introduzca el nombre del nuevo cliente: \n")
        nuevo_tel = input("Introduzca el nuevo numero de telefono: \n")
        new_telefono(nuevo_cliente, nuevo_tel)
    else:
        print("Error, numero incorrecto")
    return

def crear_listado():
    if not os.path.isfile("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali\listin.txt"):
        file = open("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali\listin.txt", "w")
        file.close()
    return
def consulta():
    return
def new_telefono(nuevo_cliente, nuevo_tel):
    with open("C:\datos\Documents\GIT_Oussama\practica0206_Rouidjali\listin.txt", "w") as file:
        texto = "\n" + nuevo_cliente + ",", nuevo_tel
        file.write(str(texto))
    return

