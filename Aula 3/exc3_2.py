x = str(input())

def contador_geral(string):
    string = string.replace('\\n',' ')
    espacos = string.count(' ')
    caracteres = len(string)
    letras = sum(1 for c in string if c.isalpha())
    numeros = sum(1 for x in string if x.isdigit())
    simbolos = caracteres - letras - numeros - espacos 
    palavras = sum(1 for x in string.split())
    
    return (caracteres,letras,numeros,simbolos + espacos ,palavras)
print (contador_geral(x))