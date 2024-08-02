entrada = eval(input())
tup = []
for i in entrada:
    tup.append(i)
n = tup[0]
a = tup[1]
b = tup[2]
c = tup[3]


def seriemat(n,a,b,c):
    result = 0
    for i in range(1,n+1):
        result += (((-1)**(c+i))*(1+a*i)/(3*(b**i)))
    result = round(result,3)
    return result
    
print (seriemat(n,a,b,c))