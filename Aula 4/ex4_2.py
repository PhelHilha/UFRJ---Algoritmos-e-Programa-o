a = eval(input())
b = eval(input())

def somamatriz(x,y):
    lA = len(x)
    lb = len(y)
    cA = len(x[0])
    cb = len(y[0])
    if lA != lb or cA != cb:
        return ("Erro!")
    for i in range(lA):
        for j in range(cA):
            x[i][j] += y[i][j]
    return (x)
    
print (somamatriz(a,b))