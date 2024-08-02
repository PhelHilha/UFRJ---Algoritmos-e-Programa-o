entrada = eval(input())

def call(x):
    escala = len(x)
    if escala == 1:
        return x
    if escala == 2:
        return matriz2x2(x)
    if escala == 3:
        return matriz3x3(x)

def matriz2x2(x):
    escala = 2
    diag = 1
    inverdiag = 1
    for i in range(escala):
        diag *= x[i][i]
        inverdiag *=  x[i][(escala-1)-i]
    return (diag - inverdiag)

def matriz3x3(x):
    escala = 3
    diag0,diag1,diag2 = 1,1,1
    inverdiag0,inverdiag1,inverdiag2 = 1,1,1
    for i in range(escala):
        diag0 *= x[i][i]
        inverdiag0 *= x[i][(escala-1)-i]
    for i in range(escala):
        diag1 *= x[i-1][i]
        inverdiag1 *= x[i-1][(escala-1)-i]
    for i in range(escala):
        diag2 *= x[i-2][i]
        inverdiag2 *= x[i-2][(escala-1)-i]

    return ((diag0+diag1+diag2) - (inverdiag0+inverdiag1+inverdiag2))

print (call(entrada))