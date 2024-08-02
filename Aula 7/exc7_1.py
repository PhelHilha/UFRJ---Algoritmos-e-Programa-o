a = eval(input())

def ordenar(l,indice = 0):
    if indice == len(l):
        return (l)
    menor = l[indice]
    for i in l[indice:]:
        if i < menor:
            menor = i
    change = l.index(menor,indice)
    l[change] = l[indice]
    l[indice] = menor
    return (ordenar(l,indice + 1))

print(ordenar(a))