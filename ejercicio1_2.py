from urllib import request
from urllib.error import URLError
lista_palabras=['puto','maricon','bobo','tonto','presenta']

def verificar_palabra(url):
    try:
        f=request.urlopen(url)
    except URLError:
        return ('La url '+url+'no existe')
    else:
        aux=f.read()
        contenido=aux.split()
        palabras_encontradas=[]
        for l in lista_palabras:
            for con in contenido:
                if l in con.decode():
                    palabras_encontradas.append(l)
        return palabras_encontradas  
url ='https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print(verificar_palabra(url))
