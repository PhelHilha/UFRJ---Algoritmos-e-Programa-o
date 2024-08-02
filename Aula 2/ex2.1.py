x = eval(input())
y = eval(input())

def f(a,b):
    #Função que retorna o produto interno de dois vetores.
    resultado = 0
    for i in range(len(a)):
        temp = a[i] * b[i]
        resultado += temp
    return resultado
    
print (f(x,y))