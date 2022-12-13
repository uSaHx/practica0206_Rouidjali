import urllib.request
def pib_eu(iniciales):
    file = urllib.request.urlopen("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
    datos = []
    for line in file:
        decoded_line = line.decode("utf-8")
        datos.append(decoded_line.split("\t"))
    for x in datos:
        for y in x:
            if iniciales in y:
                print(datos[0])
                print(x)
    return

pib_eu("AL")