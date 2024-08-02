entrada = eval(input())
caminho = entrada[0]
verificar = entrada[1]

def caminho_diagonal(m):
    n = len(m)
    c = len(m[0])
    if m[0][0] == 1 or m[n-1][c-1] == 1:
        return False
    visitados = []
    path = [(0,0)]
    atual = (0,0)
    while path:
        i,j = atual
        if (atual == (n-1,c-1)):
            return path
        if (j+1 <c and m[i][j+1] == 0 and (i,j+1) not in visitados):
            atual = (i,j+1)
            path.append(atual)
        elif (i+1<n and m[i+1][j] == 0 and (i+1,j) not in visitados):
            atual = (i+1,j)
            path.append(atual)
        else:
            visitados.append(path.pop(-1))
            atual = path[-1]
    return False

def verifica_caminho_diagonal(m,l):
    n = len(m)
    c = len(m[0])
    if not l:
        return False
    if m[0][0] == 1 or m[n-1][c-1] == 1:
        return False
    elif (l[-1] != (n-1,c-1) or l[0] != (0,0)):
        return False
    anterior = (0,0)
    for i in l:
        conta = (i[0] - anterior[0], i[1] - anterior[1])
        if (conta != (0,1) and conta != (1,0) and conta != (0,0)):
            return False
        elif (m[i[0]][i[1]] != 0):
            return False
        anterior = i
    return True
    
print((caminho_diagonal(caminho),verifica_caminho_diagonal(caminho,verificar)))