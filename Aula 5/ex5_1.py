a = eval(input())
b = eval(input())

def multmatriz(x,y):
    linB = len(y)
    colA = len(x[0])
    result = [[0 for a in range(len(y[0]))] for a in range(len(x))]

    if linB != colA:
        return ("Erro!")
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return (result)
print (multmatriz(a,b))
