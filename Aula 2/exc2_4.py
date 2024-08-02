a = int(input())
resultado = []
def digitos(x):
    value = x
    cont = 0
    while True:
        value = value / 10
        cont += 1
        if value < 1:
            break
    return cont
def invert(x):
    result = 0
    numb = x
    temp = 0
    while True:
        temp = numb%10
        result = (result*10) + temp
        numb = numb//10
        if numb < 1:
            break
    return result

resultado.append(digitos(a))
resultado.append(invert(a))

print (resultado)

        