alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
x = eval(input())
b = []
for i in x:
    b.append(i)

def indice(x,senha):
    for i in alfabeto:
        if x == i:
            if (alfabeto.index(i)+senha >= len(alfabeto)):
                return (alfabeto.index(i)+senha - len(alfabeto))
            else:
                return alfabeto.index(i)+senha
    
def codificar(string,senha):
    codificada = ""  
    for i in string:
        codificada += alfabeto[indice(i,senha)]
    return codificada

def decodificar(string,senha):
    decodificada = ""  
    for i in string:
        decodificada += alfabeto[indice(i,-senha)]
    return decodificada

def esqueciasenha(x,m,s):
    if x == True:
        return (codificar(m,s))
    if x == False:
        return (decodificar(m,s))

print(esqueciasenha(b[0],b[1],b[2]))