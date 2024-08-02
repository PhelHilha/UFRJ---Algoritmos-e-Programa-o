x= eval(input())
y= eval(input())
def recur(a,b,i=0):
    #Função que verifica a existencia de elementos iguais em dois vetores
    index = min(len(a),len(b))
    if (a[i] == b[i]):
        return True
    elif(i==index-1):
        return False
    else:
        return recur(a,b,i+1)
print (recur(x,y))