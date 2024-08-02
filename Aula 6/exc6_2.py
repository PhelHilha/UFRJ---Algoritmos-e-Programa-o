x = int(input())
y = int(input())

def recursub(a,b,i=0):
    if(b*i>a):
        return i-1
    else:
        return recursub(a,b,i+1)
print (recursub(x,y))