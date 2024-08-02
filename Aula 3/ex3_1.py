a = eval(input())
b = eval(input())

def subseq(x,y):
    total = len(x)
    restante = len(y)
    find = 0
    for i in x:
        for j in range(find,restante):
            if (i==y[j]):
                find = j+1
                total -= 1
                break
    if total == 0:
        return True
    else:
        return False
print(subseq(a,b))