import urllib.request
def contador_url(url):
   file = urllib.request.urlopen(url)
   palabras = file.readlines()
   return print(len(palabras))

contador_url("https://es.wikipedia.org/wiki/Python")