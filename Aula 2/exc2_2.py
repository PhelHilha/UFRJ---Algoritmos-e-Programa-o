x = eval(input())
y = eval(input())

def f(a,b):
    #Função que verifica a existencia de elementos iguais em dois vetores
    index = min(len(a),len(b))
    for i in range(index):
            if (a[i] == b[i]):
                return True
    return False
print (f(x,y))