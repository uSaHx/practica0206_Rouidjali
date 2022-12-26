import csv
def calificaciones():
    # Son 100 horas de clase
    # Si el alumno no tiene que realizar las recuperaciones aparece un 0 en el archivo
    resultado = leer_csv()
    resultado2 = media_examenes(resultado)
    aprobados(resultado2)
    return
def leer_csv():
    resultado = []
    with open("N:\DAPI\practica0206_Rouidjali\calificaciones.csv") as File:
        lector = csv.DictReader(File)
        for row in lector:
            resultado.append(row)
    return resultado
def media_examenes(resultado):
    with open("N:\DAPI\practica0206_Rouidjali\calificaciones.csv", "w", newline="") as file:
        campos = ["nombre", "apellido", "ex_teorico", "ex_practico", "asistencia",
                  "recu_teorico", "recu_practico", "media_examenes"]
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        resultados2 = []
        for datos in resultado:
            nota_teorico = 0
            nota_parctica = 0
            if float(datos["ex_teorico"]) >= float(datos["recu_teorico"]):
                nota_teorico = float(datos["ex_teorico"])
            else:
                nota_teorico = float(datos["recu_teorico"])
            if float(datos["ex_practico"]) >= float(datos["recu_practico"]):
                nota_parctica = float(datos["ex_practico"])
            else:
                nota_parctica = float(datos["recu_practico"])
            media = (0.3*nota_teorico) + (0.4*nota_parctica)
            datos["media_examenes"] = media
            writer.writerow(datos)
            resultados2.append(datos)
    return resultados2
def aprobados(resultados2):
    aptos = []
    no_aptos = []
    for datos in resultados2:
        if (int(datos["asistencia"]) >= 75) and (datos["media_examenes"] >= 5):
            aptos.append(datos)
        else:
            no_aptos.append(datos)
    return print(aptos), print(no_aptos)
calificaciones()
