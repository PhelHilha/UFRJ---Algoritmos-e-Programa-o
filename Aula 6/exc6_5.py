n = eval(input())


def divisores(x):
    div = set()
    for i in range(x):
        if i == 0:
            continue
        if (x%i == 0):
            div.add(i)
    return div

def divisores_comuns(tup):
    numeros = []
    for i in tup:
        numeros.append(i)
    divicom = divisores(numeros[0])
    
    for num in numeros[1:]:
        divinum = divisores(num)
        divicom = divicom.intersection(divinum)
    
    return divicom
            
    
print(divisores_comuns(n))