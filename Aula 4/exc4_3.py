entrada = eval(input())

def magic(x):
    escala = len(x)
    comparar = sum(x[0])
    coluna = [0]*escala
    diag = 0
    inverdiag = 0
    for i in range(escala):
        if (sum(x[i]) != comparar):
            return False
        else:
            comparar = sum(x[i])
    for i in range(escala):
        diag += x[i][i]
        inverdiag += x[i][(escala-1)-i]
        for j in range(escala):
            coluna[i] += x[i][j]
    if diag != comparar:
        return False
    if inverdiag != comparar:
        return False
    for i in range(escala):
        if coluna[i] != comparar:
            return False
    return True

print (magic(entrada))